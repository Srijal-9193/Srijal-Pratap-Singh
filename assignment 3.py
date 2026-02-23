# Assignment 1: Tax Calculator

income = float(input("Enter your annual income: "))
age = int(input("Enter your age: "))

# Logical operator (AND)
if age >= 60 and income > 0:
    income = income - 50000   # extra exemption for senior citizens

# if-elif ladder
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 700000:
    tax = income * 0.20
else:
    tax = income * 0.30

# Ternary operator
tax_status = "No Tax" if tax == 0 else "Tax Applicable"

print("\n----- TAX REPORT -----")
print("Taxable Income:", income)
print("Tax Amount:", tax)
print("Status:", tax_status)
