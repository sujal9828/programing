"""task 1 = Create two NumPy arrays: one representing the number of likes on your last 7 Instagram 
posts, and another for the number of comments. Use arithmetic operators to calculate the average 
engagement (likes + comments) per post and print the result.
"""

import numpy as np

likes = np.array([100, 150, 200, 120, 180, 250, 300])
comments = np.array([10, 15, 20, 12, 18, 25, 30])

engagement = likes + comments
average = np.mean(engagement)

print("Average Engagement:", average)

"""task 2 = Given two NumPy arrays: one with the prices of 5 food items on Zomato and another with 
the corresponding discounts in rupees, use element-wise subtraction to get the final price for each 
item and display the array.
"""

import numpy as np

prices = np.array([200, 300, 150, 250, 400])
discount = np.array([20, 50, 10, 30, 80])

final_price = prices - discount

print("Final Prices:", final_price)

"""task 3 =Suppose you have a NumPy array of IPL team scores for 5 matches. Use comparison operators 
to create a boolean array indicating which matches had scores greater than 180, then print the 
boolean array.<br><br><em><strong>Hint:</strong> Use the '>' operator directly on the array.</em>
"""

import numpy as np

scores = np.array([190, 175, 210, 160, 185])

result = scores > 180

print(result)
""""task 4 = Create two NumPy arrays: one showing whether a user paid via Paytm (1 for paid, 0 
for not) and another for PhonePe for 6 transactions. Use np.logical_or() to find out which 
transactions were paid by either app and print the result.
"""

import numpy as np

paytm = np.array([1, 0, 1, 0, 0, 1])
phonepe = np.array([0, 1, 1, 0, 1, 0])

result = np.logical_or(paytm, phonepe)

print(result)

""""task 5 = Given a NumPy array of the number of steps you walked each day for a week, use 
broadcasting to add a bonus of 500 steps to each day's count, then calculate and print the total 
steps for the week using an aggregate operation
"""

import numpy as np

steps = np.array([4000, 5000, 6000, 4500, 7000, 8000, 5500])

bonus_steps = steps + 500

total = np.sum(bonus_steps)

print("Steps after bonus:", bonus_steps)
print("Total Steps:", total)