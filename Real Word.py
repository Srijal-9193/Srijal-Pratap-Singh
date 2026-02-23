import pandas as pd

df = pd.read_csv('c:\\Users\\Srijal pratap singh\\Downloads\\products-100.csv')

x = df.iloc[:, :-1]  #Independent Variable
y = df.iloc[:, -1]   # Dependent variable

print("X (Independent Variables):")
print(x)
print("Y (Dependent Variable):")
print(y)

print("\nShape of X:", x.shape)
print("Shape of Y:", y.shape)

print("\nProblem Type: Regression")