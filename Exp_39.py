import pandas as pd
import numpy as np
from collections import Counter
data = {
    'Age': [25, 30, 47, 52, 46, 56, 55, 60, 35, 40],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'BloodPressure': [120, 115, 130, 135, 140, 145, 150, 160, 125, 128],
    'Cholesterol': [200, 190, 220, 210, 230, 240, 250, 260, 205, 215],
    'Outcome': ['Good', 'Good', 'Bad', 'Bad', 'Bad', 'Good', 'Bad', 'Bad', 'Good', 'Good']
}
df = pd.DataFrame(data)
df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})
X = df[['Age', 'Gender', 'BloodPressure', 'Cholesterol']].values
y = df['Outcome'].values
def normalize(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X = normalize(X)
np.random.seed(42)
indices = np.arange(len(X))
np.random.shuffle(indices)
train_size = int(0.7 * len(X))
train_idx, test_idx = indices[:train_size], indices[train_size:]
X_train, y_train = X[train_idx], y[train_idx]
X_test, y_test = X[test_idx], y[test_idx]
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
def knn_predict(X_train, y_train, x_test, k=3):
    distances = [euclidean_distance(x_test, x_train) for x_train in X_train]
    k_idx = np.argsort(distances)[:k]
    k_labels = [y_train[i] for i in k_idx]
    return Counter(k_labels).most_common(1)[0][0]
def knn_classify(X_train, y_train, X_test, k=3):
    return [knn_predict(X_train, y_train, x, k) for x in X_test]
def evaluate(y_true, y_pred, positive="Good"):
    tp = sum((yt == positive and yp == positive) for yt, yp in zip(y_true, y_pred))
    fp = sum((yt != positive and yp == positive) for yt, yp in zip(y_true, y_pred))
    fn = sum((yt == positive and yp != positive) for yt, yp in zip(y_true, y_pred))
    tn = sum((yt != positive and yp != positive) for yt, yp in zip(y_true, y_pred))
    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    return accuracy, precision, recall, f1, (tp, fp, fn, tn)
k = 3
y_pred = knn_classify(X_train, y_train, X_test, k=k)
accuracy, precision, recall, f1, (tp, fp, fn, tn) = evaluate(y_test, y_pred)
print("Prediction Results:")
print(pd.DataFrame({"Actual": y_test, "Predicted": y_pred}))
print("\nConfusion Matrix:")
print(f"TP={tp}, FP={fp}, FN={fn}, TN={tn}")
print(f"\nAccuracy: {accuracy:.4f}")
print(f" Precision: {precision:.4f}")
print(f" Recall: {recall:.4f}")
print(f" F1 Score: {f1:.4f}")