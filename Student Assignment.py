import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Srijal pratap singh\Downloads\StudentPerformance.csv', encoding='latin-1')
print("ML Problem:")
print("Predicting Student marks based on hours studied and attendance.\n")

print("Type of Learning:")
print("This is a supervised learning problem (Regression).\n")

plt.figure(figsize=(10, 6))
plt.scatter(df['Hours_Studied'], df['Marks'], color='blue')
plt.xlabel("Hours studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.show()

print("Dataset Explanation:")
print("1. The dataset contains student study-related information.")
print(df.head())
print("2. Hours_studied shows how many hurs a student studies.")
print("3. Attendence represents class attendence percentage.")
print("4. Marks is the final score obtained by the student.")
print("5. This data can be used to predict marks using regression.")