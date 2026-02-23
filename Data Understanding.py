import pandas as pd

data = {
	"Customer_ID": ["C001","C002","C003","C004","C005","C006","C007","C008","C009","C010"],
	"Age": [25, 32, 29, 41, 35, 28, 52, 47, 23, 38],
	"Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
	"City": ["Mumbai", "Pune", "Bangalore", "Delhi", "Pune", "Mumbai", "Delhi", "Bangalore", "Pune", "Mumbai"],
	"Product_Category": ["Electronics", "Clothing", "Electronics", "Home Appliances", "Groceries", "Clothing", "Electronics", "Home Appliances", "Groceries", "Electronics"],
	"Purchase_Amount": [45000, 3200, 38000, 22000, 1800, 4100, 52000, 19500, 1500, 46000],
}

numerical_columns = ["Age", "Purchase_Amount"]
categorical_columns = ["Customer_ID", "Gender", "City", "Product_Category"] 

behavioral_columns = ["Purchase_Amount", "Product_Category"]
print("Numerical Columns:", numerical_columns)
print("Categorical Columns:", categorical_columns)
print("Behavioral Columns:", behavioral_columns)

df = pd.DataFrame(data)
print(df)
