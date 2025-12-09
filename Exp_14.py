import pandas as pd
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Age": [25, 30, 25, 40, 30, 25],
    "Purchase_Amount": [200, 150, 300, 500, 250, 180]
}

df = pd.DataFrame(data)
age_frequency = df["Age"].value_counts()
print("Frequency Distribution of Customer Ages:")
print(age_frequency)
