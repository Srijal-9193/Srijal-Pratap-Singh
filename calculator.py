# Calculator Module

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

a = 15
b = 5

print("Addition:", addition(a, b))
print("Subtraction:", subtraction(a, b))
print("Multiplication:", multiplication(a, b))
print("Division:", division(a, b))
