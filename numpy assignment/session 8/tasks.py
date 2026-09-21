"""task 1 = Given a NumPy array of IPL team names with some duplicates, use np.unique() to print a 
sorted list of all unique team names. 
"""

import numpy as np

teams = np.array([
    "CSK", "MI", "RCB", "CSK", "KKR",
    "MI", "GT", "RCB", "GT"
])

unique_teams = np.unique(teams)

print(unique_teams)


""" task 2 = Create a NumPy array of Zomato order ratings (with some NaN values), then use np.isnan()
to count how many ratings are missing.
"""

import numpy as np

ratings = np.array([4.5, 4.2, np.nan, 3.8, np.nan, 4.7, 4.0])

missing = np.isnan(ratings)

print("Missing values:", missing)
print("Number of missing ratings:", np.sum(missing))


""" task 3 = 
Given an array of Flipkart product prices, use np.clip() to limit all prices between 100 and 1000, 
and print the resulting array.<br><br><em><strong>Hint:</strong> Use np.clip(array, 100, 1000).
</em>
"""

import numpy as np

prices = np.array([50, 150, 500, 1200, 800, 2000, 750])

result = np.clip(prices, 100, 1000)

print(result)


"""task 4 = You have a NumPy array of YouTube video view counts, some of which are NaN or inf. 
Replace all NaN values with 0, and all inf values with the maximum finite value in the array.
"""

import numpy as np

views = np.array([1000, 2500, np.nan, 5000, np.inf, 3000, np.nan])

# Maximum finite value
max_value = np.nanmax(views[np.isfinite(views)])

# Replace NaN with 0
views[np.isnan(views)] = 0

# Replace infinity with maximum finite value
views[np.isinf(views)] = max_value

print(views)


"""task 5 = Use ChatGPT to generate a Python code snippet that finds the indices of all even numbers 
in a NumPy array using np.where(), then test the code with your own example array.
"""

import numpy as np

numbers = np.array([11, 24, 35, 42, 57, 68, 73, 80])

even_indices = np.where(numbers % 2 == 0)

print("Even number indices:", even_indices[0])