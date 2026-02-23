n = int(input("Enter number of students: "))

marks = []
fail_count = 0

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

    if m < 23:
        fail_count += 1

# Average calculation
average = sum(marks) / n

print("\n--- Result ---")
print("Marks of students:", marks)
print("Average Marks:", average)
print("Number of Failed Students:", fail_count)
