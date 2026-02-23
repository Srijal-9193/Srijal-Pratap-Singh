n = int(input("Enter how many numbers: "))

numbers = []
positive = 0
negative = 0
zero = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

    if num > 0:
        positive += 1

    elif num < 0:
        negative += 1
        
    else:
        zero += 1

largest = max(numbers)
smallest = min(numbers)

print("\n--- Result ---")
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Largest number:", largest)
print("Smallest number:", smallest)
