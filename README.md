# 🏦 Loan Approval Predictor

**🔗 Live Demo:** [Try the App](https://loan-approval-predictor-xr70.onrender.com)

---

## 📌 Overview

The **Loan Approval Predictor** is a machine learning web application that determines whether a loan application is likely to be **approved or rejected**, based on user-provided information. It is built with a **supervised learning model**, a Flask-powered backend, and a clean frontend using HTML and CSS.

---

## 🧠 How It Works

1. User enters loan applicant details (e.g., income, credit history, loan amount).
2. Inputs are preprocessed (categorical encoding, missing value handling, scaling).
3. A trained ML model makes a real-time prediction on approval status.
4. The result is displayed instantly on the screen.

---

## 🚀 Key Features

- ✅ Real-time loan approval prediction
- 🔍 Clean, minimal UI with a responsive design
- 📊 Supports categorical and numerical input
- 🛠️ Backend ML pipeline integrated with Flask
- 💾 Model saved using Pickle for quick deployment

---

## 🛠️ Tech Stack

### ⚙️ Machine Learning & Backend
- **Python**, **Pandas**, **NumPy** – Data handling & preprocessing
- **Scikit-learn** – Model training & inference
- **Pickle** – Model serialization
- **Flask** – Web backend and routing

### 🌐 Frontend
- **HTML** – Form-based input interface
- **CSS** – Styling and responsive layout

---

## 🧪 Data & Preprocessing

- Handled missing values and cleaned inconsistencies
- Encoded categorical variables (e.g., Gender, Marital Status)
- Scaled numerical features (e.g., Income, Loan Amount)
- Trained on a labeled dataset with known approval outcomes

---

1. **Clone the Repository**

```git clone https://github.com/yourusername/loan-approval-predictor.git```

```cd loan-approval-predictor```

2. **Install Dependencies**

```pip install -r requirements.txt```

3. **Run the Flask App**

```python app.py```
