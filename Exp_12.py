import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Temperature": [15, 17, 20, 25, 30, 32, 31, 30, 28, 24, 20, 16],  # in °C
    "Rainfall": [40, 35, 50, 70, 120, 150, 180, 160, 110, 60, 45, 30]  # in mm
}

df = pd.DataFrame(data)
plt.figure(figsize=(7,4))
plt.plot(df["Month"], df["Temperature"])
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Line Plot")
plt.show()
plt.figure(figsize=(7,4))
plt.scatter(df["Month"], df["Rainfall"])
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall Scatter Plot")
plt.show()
