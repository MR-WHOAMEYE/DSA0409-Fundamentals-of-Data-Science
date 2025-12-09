import numpy as np

# Example 3x3 matrix (each row = sales for a product)
sales_data = np.array([
    [120, 150, 130],
    [80,  90,  100],
    [200, 180, 160]
])

avg_price = np.mean(sales_data)
print("Average price:", avg_price)
