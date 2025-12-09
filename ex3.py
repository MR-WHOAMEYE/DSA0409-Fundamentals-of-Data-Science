import numpy as np

house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 420000],
    [4, 1800, 300000],
    [6, 2600, 510000]
])

filtered = house_data[house_data[:, 0] > 4]

avg_price = np.mean(filtered[:, 2])
print("Average sale price:", avg_price)
