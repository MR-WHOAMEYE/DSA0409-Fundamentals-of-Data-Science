from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
data = load_iris()
X_full = data.data
y_full = data.target
feature_names = data.feature_names
target_names = data.target_names
print("\nAvailable Features:")
for i, f in enumerate(feature_names):
    print(f"{i}: {f}")
selected = input("\nEnter feature indices separated by commas (e.g., 0,2): ")
selected_idx = [int(i) for i in selected.split(",")]
X = X_full[:, selected_idx]
y = y_full
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average="weighted")
rec = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")
print("\n--- Model Evaluation ---")
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall:    {rec:.4f}")
print(f"F1-Score:  {f1:.4f}")