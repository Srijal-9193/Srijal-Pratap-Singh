import pandas as pd

df = pd.read_csv('c:\\Users\\Srijal pratap singh\\Downloads\\products-100.csv')

print("Column names:")
print(df.columns)

X = df.iloc[:, :-1]  # all columns except the last one
y = df.iloc[:, -1]   # the last column

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)

print("\nX Data:")
print(X)

print("\ny Data:")
print(y)