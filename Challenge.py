import pandas as pd

df = pd.read_csv('c:\\Users\\Srijal pratap singh\\Downloads\\products-100.csv')

print("Feature Removal Analysis\n")

print("Original Independent Variables:")
print("- Area(sqft)")
print("- Bedrooms")
print("- Bathrooms")
print("- House Age")

print("\nRemoved Independent Variable:")
print("- House Age")

print("\nPredicted Impact on Model Accuracy:")
print("Model accuracy is expected to decrease.")

print("\nReasoning:")
print("House age has a strong effect on house price.")
print("Removing this feature reduces information available to the model.")
print("Less information leads to less accurate predictions.")

print("\nFinal Conclusion:")
print("Removing an important independent variable decreases modal accuracy.")