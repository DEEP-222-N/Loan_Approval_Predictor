from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
import os

app = Flask(__name__)
app.secret_key = "9f1c4e2d3b6a4c3d9e8f7a6b5c4d3e3f"

# Load the model
MODEL_PATH = os.path.join("model", "Best_AdaBoost_Model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form.to_dict()

        try:
            # Prepare input
            dependents = form_data.get("Dependents")
            dependents = 3 if dependents == "3+" else int(dependents)

            area = form_data.get("Property_Area")
            semiurban = 1 if area == "Semiurban" else 0
            urban = 1 if area == "Urban" else 0

            applicant_income = float(form_data.get("ApplicantIncome"))
            coapplicant_income = float(form_data.get("CoapplicantIncome"))
            loan_amount = float(form_data.get("LoanAmount"))
            loan_term = float(form_data.get("Loan_Amount_Term"))
            credit_history = int(form_data.get("Credit_History"))

            total_income = applicant_income + coapplicant_income
            emi = loan_amount / (loan_term)
            affordable = emi <= 0.4 * total_income 

            features = [
                int(form_data.get("Gender")),
                int(form_data.get("Married")),
                dependents,
                int(form_data.get("Education")),
                int(form_data.get("Self_Employed")),
                applicant_income,
                coapplicant_income,
                loan_amount,
                credit_history,
                loan_term,
                semiurban,
                urban
            ]

            input_data = np.array(features).reshape(1, -1)

            # Decision logic
            if not affordable:
                result = 0
            else:
                result = model.predict(input_data)[0]

            prediction = "✅ Loan Approved" if result == 1 else "❌ Loan Rejected"

            # Reasoning for rejection
            reason = None
            if result == 0:
                reasons = []
                if credit_history == 0:
                    reasons.append("Poor credit history.")
                if not affordable:
                    reasons.append(f"EMI ₹{emi:.2f} exceeds 40% of income ₹{total_income:.2f}.")
                if total_income < 2500:
                    reasons.append("Total income too low.")
                if loan_amount > total_income * 0.5:
                    reasons.append("Loan amount too high compared to income.")
                if not reasons:
                    reasons.append("Failed to meet loan approval criteria.")
                reason = " ".join(reasons)

            # Store for displaying after redirect
            session['form_data'] = form_data
            session['prediction'] = prediction
            session['reason'] = reason

            return redirect(url_for("index"))

        except Exception as e:
            return f"An error occurred: {e}", 500

    # On GET request
    form_data = session.pop("form_data", {})
    prediction = session.pop("prediction", None)
    reason = session.pop("reason", None)

    return render_template("index.html", form_data=form_data, prediction=prediction, reason=reason)

if __name__ == "__main__":
    app.run(debug=True)
