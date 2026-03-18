import pandas as pd
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv("data/fraud.csv")

# Encode categorical
le = LabelEncoder()
data['type'] = le.fit_transform(data['type'])

# Features & target
X = data.drop("isFraud", axis=1)
y = data["isFraud"]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Logistic": LogisticRegression(),
    "DecisionTree": DecisionTreeClassifier(),
    "RandomForest": RandomForestClassifier()
}

best_model = None
best_score = 0

print("----- Model Comparison -----")

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    score = f1_score(y_test, pred)
    
    print(f"{name} F1 Score:", score)
    
    if score > best_score:
        best_score = score
        best_model = model

# Hyperparameter tuning (Random Forest)
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, None]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)
grid.fit(X_train, y_train)

best_rf = grid.best_estimator_

# Final prediction
final_pred = best_rf.predict(X_test)

print("\nFinal Model Performance:")
print("Accuracy:", accuracy_score(y_test, final_pred))
print("F1 Score:", f1_score(y_test, final_pred))
print("\nReport:\n", classification_report(y_test, final_pred))

# Save model + scaler + encoder
pickle.dump(best_rf, open("models/model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(le, open("models/encoder.pkl", "wb"))

print("\nModel saved successfully!")