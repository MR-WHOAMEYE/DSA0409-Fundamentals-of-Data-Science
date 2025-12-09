import numpy as np

sales_data = np.array([120000, 150000, 170000, 210000])

total_sales = np.sum(sales_data)

pct_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total sales:", total_sales)
print("Percentage increase Q1 → Q4:", pct_increase)
