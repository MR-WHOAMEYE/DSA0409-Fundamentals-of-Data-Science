from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([
    [1200, 2, 10],
    [1500, 3, 5],
    [1800, 3, 2],
    [900,  2, 20],
    [2000, 4, 1],
    [1100, 2, 15]
])
y = np.array([45, 60, 75, 38, 90, 42])
model = LinearRegression()
model.fit(X, y)
print("Enter new house details:")
area = float(input("Area in sqft: "))
bedrooms = int(input("Number of bedrooms: "))
age = float(input("Age of the house (years): "))
new_house = np.array([[area, bedrooms, age]])
predicted_price = model.predict(new_house)[0]
print("\n--- Predicted Price ---")
print(f"Estimated price: {predicted_price:.2f} lakhs")