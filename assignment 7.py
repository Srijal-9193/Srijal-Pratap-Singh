#pattern Generator
1. #Square Pattern

# Example usage of square function
n = int(input("Enter size of square: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

2. #Triangle Pattern

n = int(input("Enter size of triangle: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

3. #Pyramid Pattern    

n = int(input("Enter size of pyramid: "))
for i in range(n):
    for space in range(n-i-1):
        print(" ", end="")
    for star in range(2*i+1):
        print("*", end="")
    print()