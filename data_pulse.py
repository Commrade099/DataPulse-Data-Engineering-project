import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

print("DataPulse Started")

# Load CSV
data = pd.read_csv("data.csv")

print("\nData Loaded:")
print(data)

# Connect to SQL
conn = sqlite3.connect("database.db")

# Store data
data.to_sql("employees", conn, if_exists="replace", index=False)

print("\nData stored in SQL database")

# Read back from SQL
result = pd.read_sql("SELECT * FROM employees", conn)

print("\nReport:")
print(result.describe())

conn.close()

# Visualization
plt.bar(data['name'], data['salary'])
plt.title("Salary Distribution")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()

print("\nProcess Completed")