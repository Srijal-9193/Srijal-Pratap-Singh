# Sort list using lambda function
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted List:", sorted_numbers)

# Filter even numbers using lambda function

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)