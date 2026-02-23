# Assignment 2: Business Rule Engine

salary = float(input("Enter annual salary: "))
experience = int(input("Enter experience in years: "))

# Ternary Operator (experience-based exemption)
exemption = 100000 if experience >= 7 else 0

taxable_salary = salary - exemption

# Business rules using conditions
if taxable_salary <= 300000:
    tax = 0
elif taxable_salary <= 600000:
    tax = taxable_salary * 0.10
elif taxable_salary <= 1000000:
    tax = taxable_salary * 0.20
else:
    tax = taxable_salary * 0.30

# Ternary operator for status
tax_status = "No Tax" if tax == 0 else "Tax Applicable"

print("\n----- BUSINESS RULE ENGINE OUTPUT -----")
print("Original Salary:", salary)
print("Experience:", experience, "years")
print("Exemption Applied:", exemption)
print("Taxable Salary:", taxable_salary)
print("Tax Amount:", tax)
print("Tax Status:", tax_status)
