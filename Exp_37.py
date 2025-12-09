import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'HouseSize': [850, 900, 1200, 1500, 1700, 2000, 2200, 2500],
    'Price':     [150000, 160000, 200000, 250000, 280000, 320000, 350000, 400000]
}
df = pd.DataFrame(data)
X = df['HouseSize'].values
y = df['Price'].values
X_mean = np.mean(X)
y_mean = np.mean(y)
b1 = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
b0 = y_mean - b1 * X_mean
print(f"Regression Equation: Price = {b0:.2f} + {b1:.2f}*HouseSize")
y_pred = b0 + b1 * X
