from sklearn.neighbors import KNeighborsClassifier
import numpy as np
X = np.array([
    [2.5, 1.2, 3.4],
    [1.0, 0.8, 2.1],
    [3.6, 2.5, 4.1],
    [0.9, 1.0, 1.8],
    [4.1, 3.0, 4.5],
    [2.2, 1.5, 2.9]
])
y = np.array([0, 0, 1, 0, 1, 1])
k = int(input("Enter value of k (number of neighbors): "))
print("Enter patient symptom values:")
new_patient = []
for i in range(X.shape[1]):
    val = float(input(f"Feature {i+1}: "))
    new_patient.append(val)
new_patient = np.array(new_patient).reshape(1, -1)
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)
prediction = knn.predict(new_patient)[0]
print("\n--- Prediction Result ---")
if prediction == 1:
    print("The patient is predicted to HAVE the medical condition.")
else:
    print("The patient is predicted to NOT have the medical condition.")