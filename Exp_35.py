import numpy as np
house_data = np.array([
    [3, 1800, 250000],
    [5, 2500, 400000],
    [4, 2000, 320000],
    [6, 3000, 500000],
    [2, 1500, 200000]
])
houses_with_more_than_4 = house_data[house_data[:, 0] > 4]
sale_prices = houses_with_more_than_4[:, -1]
average_price = np.mean(sale_prices)
print("Average sale price of houses with more than 4 bedrooms:", average_price)