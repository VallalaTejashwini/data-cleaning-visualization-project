import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("students.csv")

# Handle missing values
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Marks"] = data["Marks"].fillna(data["Marks"].mean())
data["City"] = data["City"].fillna("Unknown")

# Remove duplicates
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("cleaned_students.csv", index=False)

print("Cleaned dataset saved successfully")

# Create bar chart
plt.figure(figsize=(8,5))

sns.barplot(x="Name", y="Marks", data=data)

plt.title("Student Marks Comparison")

plt.show()