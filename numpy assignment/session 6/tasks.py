"""task 1 = Create a NumPy array called prices with the following values: [199, 299, 399, 499, 599]
. Use basic indexing to print the first and last price.
"""

import numpy as np

prices = np.array([199, 299, 399, 499, 599])

print("First price:", prices[0])
print("Last price:", prices[-1])


"""task 2 = 
Given a 2D NumPy array representing cricket scores for 3 players across 5 matches, use slicing to 
extract the scores of all players for matches 2 to 4 (index 1 to 3)
"""

import numpy as np

scores = np.array([
    [80, 85, 90, 88, 95],
    [75, 82, 89, 91, 87],
    [90, 92, 85, 88, 94]
])

result = scores[:, 1:4]

print(result)

"""task 3 = You have a NumPy array called ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5]). 
Use negative indexing to print the last three ratings.
"""

import numpy as np

ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

print(ratings[-3:])


"""task 4 = Create a NumPy array of the first 20 natural numbers. Use step slicing to print every 
3rd number starting from the second element.<br><br><em><strong>Hint:</strong> Use the slice 
notation with a step value.</em>
"""

import numpy as np

numbers = np.arange(1, 21)

print(numbers[1::3])


"""task 5 = Given a NumPy array of Flipkart product prices, use boolean indexing to extract all 
prices greater than 500. Print the resulting array.
"""

import numpy as np

prices = np.array([250, 600, 450, 800, 300, 750, 550])

result = prices[prices > 500]

print(result)


"""task 6 = 
You have an array of IPL team scores: np.array([210, 180, 195, 220, 205, 175]). Use np.where() to 
find the indices of all scores above 200 and print these indices.
"""

import numpy as np

scores = np.array([210, 180, 195, 220, 205, 175])

result = np.where(scores > 200)

print(result)