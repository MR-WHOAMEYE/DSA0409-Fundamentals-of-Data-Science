import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1500, 1700, 1600, 1800, 2000]
}
df = pd.DataFrame(data)
plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Plot")
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Scatter Plot")
plt.show()
plt.figure(figsize=(6,4))
df.plot(kind="bar", x="Month", y="Sales", legend=False)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Bar Plot")
plt.show()
