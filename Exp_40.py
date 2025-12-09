import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8],
    'TotalSpent': [500, 1500, 700, 3000, 2500, 800, 1200, 4000],
    'Frequency':  [5, 15, 7, 30, 25, 9, 12, 40]
}
df = pd.DataFrame(data)
X = df[['TotalSpent', 'Frequency']].values
def initialize_centroids(X, k):
    np.random.seed(42)
    random_idx = np.random.choice(len(X), k, replace=False)
    return X[random_idx]
def assign_clusters(X, centroids):
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)
def update_centroids(X, labels, k):
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])
def kmeans(X, k, max_iters=100, tol=1e-4):
    centroids = initialize_centroids(X, k)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)
        if np.all(np.abs(new_centroids - centroids) < tol):
            break
        centroids = new_centroids
    return labels, centroids
k = 3
labels, centroids = kmeans(X, k)
df['Cluster'] = labels
print("Clustered Data:\n", df)
print("\nCluster Centers:\n", centroids)
colors = ['red', 'blue', 'green']
for i in range(k):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], c=colors[i], label=f"Cluster {i}")
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=200, label="Centroids")
plt.xlabel("Total Amount Spent")
plt.ylabel("Frequency of Visits")
plt.title("Customer Segmentation using K-Means")
plt.legend()
plt.show()