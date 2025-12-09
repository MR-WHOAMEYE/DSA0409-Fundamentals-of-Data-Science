import pandas as pd
order_data = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 104],
    "order_date": [
        "2025-01-05",
        "2025-01-06",
        "2025-01-07",
        "2025-01-10",
        "2025-01-12",
        "2025-01-14"
    ],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Monitor"],
    "order_quantity": [1, 2, 1, 1, 3, 1]
})
print(order_data)
print("/n")
total_orders_per_customer = order_data.groupby("customer_id").size()
print("Total Number of Orders made by each customer",total_orders_per_customer)
print("\n")
avg_quantity_per_product = order_data.groupby("product_name")["order_quantity"].mean()
print("Average Order Quantity for each product",avg_quantity_per_product)
print("\n")
order_data["order_date"] = pd.to_datetime(order_data["order_date"], errors="coerce")
earliest_date = order_data["order_date"].min()
latest_date = order_data["order_date"].max()
print("Earliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)