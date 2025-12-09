import numpy as np
np.random.seed(42)
purchase_freq = np.random.randint(1, 20, size=100)
avg_spend = np.random.uniform(100, 1000, size=100)
time_on_site = np.random.uniform(5, 60, size=100)
X = np.column_stack((purchase_freq, avg_spend, time_on_site))
k = 3
max_iters = 100
centroids = X[np.random.choice(len(X), k, replace=False)]
for _ in range(max_iters):
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)
    new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids
print("Enter shopping-related features of the new customer:")
freq_input = float(input("Purchase frequency (per month): "))
spend_input = float(input("Average spend per purchase (₹): "))
time_input = float(input("Average time on site (minutes): "))
new_customer = np.array([freq_input, spend_input, time_input])
distances_to_centroids = np.linalg.norm(centroids - new_customer, axis=1)
assigned_cluster = np.argmin(distances_to_centroids)
print(f"\n The new customer belongs to Segment {assigned_cluster}")