from sklearn.cluster import KMeans
import numpy as np
X = np.array([
    [20000,  5, 1500],
    [35000, 10, 2500],
    [12000,  3,  800],
    [50000, 15, 3000],
    [18000,  4, 1200],
    [40000, 12, 2800],
    [9000,   2,  600],
    [30000,  9, 2200]
])
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
print("K-Means model trained on existing customer data.\n")
print("Enter new customer shopping details:")
annual_spend = float(input("Annual spend (in currency units): "))
visit_freq = float(input("Number of visits per month: "))
avg_cart = float(input("Average cart value per visit: "))
new_customer = np.array([[annual_spend, visit_freq, avg_cart]])
cluster_label = kmeans.predict(new_customer)[0]
print("\n--- Segmentation Result ---")
print(f"The new customer belongs to Segment: {cluster_label}")
print("\nCluster centers (for reference):")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"Segment {i}: {center}")