# Import pandas library
import sys
import subprocess

try:
    import importlib
    pd = importlib.import_module("pandas")
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import importlib
    pd = importlib.import_module("pandas")

# Create DataFrame
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Pooja", "Karan"],
    "Marks": [78, 45, 88, 32, 67]
}

df = pd.DataFrame(data)

# Calculate average, max, min
average_marks = df["Marks"].mean()
max_marks = df["Marks"].max()
min_marks = df["Marks"].min()

print("Average Marks:", average_marks)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)

# Add Result column (Pass if marks >= 40 else Fail)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nFinal DataFrame:")
print(df)
