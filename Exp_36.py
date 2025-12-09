import pandas as pd
import numpy as np
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6],
    'Age': [25, 34, 45, 23, 35, 52],
    'Annual_Income': [35000, 54000, 60000, 30000, 58000, 80000],
    'Spending_Score': [40, 60, 65, 30, 62, 80]
}
df = pd.DataFrame(data)
X = df[['Age', 'Annual_Income', 'Spending_Score']].values
def initialize_centroids(X, k):
    """Randomly pick k centroids from data points"""
    np.random.seed(42)
    random_idx = np.random.permutation(X.shape[0])[:k]
    return X[random_idx]
def assign_clusters(X, centroids):
    """Assign points to the nearest centroid"""
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)
def update_centroids(X, labels, k):
    """Recalculate centroids as mean of assigned points"""
    new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    return new_centroids
def has_converged(old_centroids, new_centroids, tol=1e-4):
    """Check if centroids have converged"""
    return np.all(np.abs(new_centroids - old_centroids) < tol)
def kmeans(X, k, max_iters=100):
    centroids = initialize_centroids(X, k)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)
        if has_converged(centroids, new_centroids):
            break
        centroids = new_centroids
    return labels, centroids
k=3
labels, centroids = kmeans(X, k)
df['Cluster'] = labels
print("Clustered Data:")
print(df)
print("\nCluster Centers:")
print(centroids)