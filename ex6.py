import numpy as np
prices=np.array([100, 50, 30])
quantities=np.array([2, 1, 3])
discount=10
tax=5
total_price=np.sum(prices*quantities)
discount_amount = total_price * (discount / 100)
price_after_discount = total_price - discount_amount
tax_amount = price_after_discount * (tax / 100)
final_amount = price_after_discount + tax_amount
print("Final Amount:", final_amount)
