import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("customers.csv")
features = data[["age", "annual_income", "spending_score"]]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
k=4
kmeans = KMeans(n_clusters=k, random_state=42)
data["cluster"] = kmeans.fit_predict(scaled_features)
print("First 10 customers with their clusters:")
print(data[["customer_id", "age", "annual_income", "spending_score", "cluster"]].head(10))
print("\nCluster-wise average values:")
print(data.groupby("cluster")[["age", "annual_income", "spending_score"]].mean())