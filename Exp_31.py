import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
data = pd.read_csv("car_data.csv")
data["brand"] = data["brand"].astype("category").cat.codes
data["engine_type"] = data["engine_type"].astype("category").cat.codes
X = data[["mileage", "age", "brand", "engine_type"]]
y = data["price"]
model = DecisionTreeRegressor()
model.fit(X, y)
mileage = float(input("Enter mileage: "))
age = float(input("Enter age: "))
brand = int(input("Enter brand code (check dataset): "))
engine = int(input("Enter engine type code (check dataset): "))
new_car = [[mileage, age, brand, engine]]
pred_price = model.predict(new_car)[0]
print("\nPredicted Price:", pred_price)
print("\nDecision Path:")
tree_rules = export_text(model, feature_names=["mileage", "age", "brand", "engine_type"])
print(tree_rules)