from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np
iris = load_iris()
X = iris.data
y = iris.target
species = iris.target_names
model = DecisionTreeClassifier()
model.fit(X, y)
print("Enter the flower measurements:")
sepal_length = float(input("Sepal length: "))
sepal_width = float(input("Sepal width: "))
petal_length = float(input("Petal length: "))
petal_width = float(input("Petal width: "))
new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(new_flower)[0]
predicted_species = species[prediction]
print("\n--- Prediction Result ---")
print(f"The predicted species is: {predicted_species}")