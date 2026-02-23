import pandas as pd

data = {
  'Age': [25, 32, 29, 41, 35, 28, 52, 47,],
  'Experience': [2, 8, 5, 15, 10, 3, 30, 20],
  'salary': [50000, 80000, 60000, 120000, 90000, 55000, 150000, 110000]
}

df = pd.DataFrame(data)

X = df[['Age', 'Experience']] 

y = df['salary']  # Selecting dependent variable

print("X (Independent Variables):")
print(X)

print("y (Dependent Variable):")
print(y)