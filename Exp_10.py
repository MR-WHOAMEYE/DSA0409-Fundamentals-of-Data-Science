import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 17000, 21000, 25000]
}
df = pd.DataFrame(data)
df.plot(x="Month", y="Sales", kind="line", marker='o', figsize=(8,5), title="Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
df.plot(x="Month", y="Sales", kind="bar", color="orange", figsize=(8,5), title="Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
