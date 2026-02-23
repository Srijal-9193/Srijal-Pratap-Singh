import matplotlib.pyplot as plt

expenses = ["Rent", "Food", "Travel", "Entertainment", "Savings"]
amount = [4000, 2500, 1200, 800, 1500]

plt.pie(amount, labels=expenses, autopct="%1.1f%%")
plt.title("Monthly Expense Distribution")
plt.show()
