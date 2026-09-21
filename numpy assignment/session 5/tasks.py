"""task 1 = Create two NumPy arrays representing the number of likes on your last 7 Instagram posts 
and your friend's last 7 posts, then use np.add() and np.subtract() to calculate both the combined 
and difference arrays.
"""

import numpy as np

my_likes = np.array([100, 150, 200, 250, 300, 350, 400])
friend_likes = np.array([120, 140, 180, 270, 290, 330, 420])

combined = np.add(my_likes, friend_likes)
difference = np.subtract(my_likes, friend_likes)

print("Combined Likes:", combined)
print("Difference:", difference)

"""task 2 = Given a NumPy array of item prices from your last Zomato order, use np.multiply() to 
apply a 10% discount on each item, then use np.sum() to calculate the final bill amount after 
discount.<br><br><em><strong>Hint:</strong> To apply a 10% discount, multiply each price by 
0.9.</em>
"""

import numpy as np

prices = np.array([200, 150, 300, 250, 100])

final_prices = np.multiply(prices, 0.9)
bill = np.sum(final_prices)

print("Prices after discount:", final_prices)
print("Final Bill:", bill)

"""task 3 = Take a NumPy array of daily step counts for the last 30 days (you can make up the numbers),
and use np.mean(), np.median(), np.std(), and np.max() to analyze your fitness stats like a health 
app would.
"""

import numpy as np

steps = np.array([
    5000, 6500, 7000, 4500, 8000,
    9000, 7500, 6000, 5500, 8500,
    7000, 7200, 6800, 5000, 9500,
    10000, 6500, 7800, 8200, 6000,
    5500, 7000, 7600, 8800, 9200,
    6400, 7100, 8000, 8500, 9000
])

print("Average Steps:", np.mean(steps))
print("Median Steps:", np.median(steps))
print("Standard Deviation:", np.std(steps))
print("Maximum Steps:", np.max(steps))


"""task 4 = Create a NumPy array of 10 random float ratings (between 1 and 5) for a new movie on 
BookMyShow, then use np.round(), np.floor(), and np.ceil() to show how the rating would appear if
rounded to the nearest whole number, always rounded down, and always rounded up.
"""

import numpy as np

ratings = np.array([4.2, 3.7, 4.8, 2.9, 3.5, 4.1, 4.6, 2.4, 3.9, 4.7])

print("Original Ratings:", ratings)
print("Rounded:", np.round(ratings))
print("Floor:", np.floor(ratings))
print("Ceil:", np.ceil(ratings))


"""task 5 = 
Use ChatGPT to generate Python code that calculates the percentage of songs you skipped in your 
last 20 Spotify plays using NumPy arrays and np.percentile(), then run the code and paste your 
output.<br><br><em><strong>Hint:</strong> Ask ChatGPT for code that finds the 75th percentile of 
skips in a NumPy array.</em>
"""

import numpy as np

skips = np.array([
    1, 0, 1, 0, 0,
    1, 0, 0, 1, 0,
    0, 1, 0, 0, 1,
    0, 0, 1, 0, 1
])

percentage = np.mean(skips) * 100
percentile_75 = np.percentile(skips, 75)

print("Skip Percentage:", percentage)
print("75th Percentile:", percentile_75)

