import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = [85, 78, 88, 74, 90]

plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks")
plt.show()
