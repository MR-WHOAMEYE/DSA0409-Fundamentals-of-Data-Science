from sklearn.linear_model import LogisticRegression
import numpy as np
X = np.array([
    [200, 12, 1],
    [350, 24, 0],
    [120,  6, 3],
    [400, 36, 1],
    [150,  3, 4],
    [300, 18, 2]
])
y = np.array([0, 0, 1, 0, 1, 0])
model = LogisticRegression()
model.fit(X, y)
print("Enter new customer details:")
usage = float(input("Monthly usage minutes: "))
contract = float(input("Contract duration (months): "))
support = int(input("Number of support calls: "))

new_customer = np.array([[usage, contract, support]])
prediction = model.predict(new_customer)[0]
prob = model.predict_proba(new_customer)[0][1]
print("\n--- Prediction Result ---")
if prediction == 1:
    print("Prediction: Customer WILL CHURN.")
else:
    print("Prediction: Customer WILL NOT CHURN.")
print(f"Churn Probability: {prob:.4f}")