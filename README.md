# 🚀 Fraud Detection System (ML Project)

## 📌 Problem Statement
Online transactions me fraud ka risk bahut zyada hai.  
Is project ka goal fraudulent transactions detect karna hai using ML.

## 👥 Who Faces This Problem
- Banks
- Fintech companies
- Customers

## 💡 Solution
Machine Learning model predicts:
- 1 → Fraud
- 0 → Safe

## 📊 Dataset
- Custom dataset (transaction data)
- Features:
  - amount
  - oldbalance
  - newbalance
  - type

## ⚙️ Approach
1. Data preprocessing
2. Encoding categorical data
3. Feature scaling
4. Train-test split
5. Model training

## 🤖 Models Used
- Logistic Regression
- Decision Tree
- Random Forest

## 📈 Evaluation Metrics
- Accuracy
- F1 Score
- Classification Report

## 🏆 Best Model
Random Forest (highest performance)

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/train_model.py
cd app
python main.py