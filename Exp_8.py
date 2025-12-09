import pandas as pd
sales_data = pd.DataFrame({
    "product_name": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Mouse", "Laptop", "Keyboard", "Monitor", "Mouse",
        "Headphones", "Headphones", "Laptop", "Keyboard"
    ],
    "quantity_sold": [5, 12, 8, 4, 7, 10, 6, 5, 3, 8, 15, 9, 4, 7]
})
print("Sample sales data",sales_data)
print("\n")
top_5_products = (
    sales_data.groupby("product_name")["quantity_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("Top 5 Most Sold products",top_5_products)
