# Salary Eligibility Checker

print("----- Salary Eligibility Checker -----")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))

if age > 21:
    print("\nHello", name)
    print("You are eligible based on your age.")
else:
    print("\nHello", name)
    print("You are not eligible based on your age.")
if salary >= 30000:
    print("\nHello", name)
    print("You are eligible based on your salary.")
else:
    print("\nHello", name)
    print("You are not eligible based on your salary.")
