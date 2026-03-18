import pickle
import numpy as np

# Load files
model = pickle.load(open("../models/model.pkl", "rb"))
scaler = pickle.load(open("../models/scaler.pkl", "rb"))
encoder = pickle.load(open("../models/encoder.pkl", "rb"))

print("Enter transaction details:")

amount = float(input("Amount: "))
oldbalance = float(input("Old Balance: "))
newbalance = float(input("New Balance: "))
type_input = input("Type (payment/transfer/cash_out): ")

# Encode type
type_encoded = encoder.transform([type_input])[0]

# Prepare input
data = np.array([[amount, oldbalance, newbalance, type_encoded]])
data_scaled = scaler.transform(data)

# Prediction
result = model.predict(data_scaled)

if result[0] == 1:
    print("⚠ Fraud Detected")
else:
    print("✅ Safe Transaction")