# Student Utility Functions

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

marks = [78, 85, 90, 66, 88]

print("Average Marks:", average_marks(marks))
print("Highest Marks:", highest_marks(marks))
