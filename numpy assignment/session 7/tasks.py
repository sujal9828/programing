"""task 1 = 
Create two NumPy arrays representing the ratings of 5 restaurants on Zomato and Swiggy, then use 
np.concatenate() to combine them into a single array of 10 ratings and print the result.
"""

import numpy as np

zomato = np.array([4.2, 4.5, 3.8, 4.7, 4.0])
swiggy = np.array([4.1, 4.6, 3.9, 4.4, 4.3])

result = np.concatenate((zomato, swiggy))

print("Combined Ratings:", result)


"""task 2 = Given three arrays representing the number of likes on three different Instagram posts 
over 7 days, stack them vertically using np.vstack() so that each row represents one post's weekly 
likes, and print the stacked array.
"""

import numpy as np

post1 = np.array([100, 120, 150, 180, 200, 220, 250])
post2 = np.array([80, 110, 130, 160, 190, 210, 230])
post3 = np.array([90, 100, 140, 170, 210, 240, 280])

result = np.vstack((post1, post2, post3))

print(result)


"""task 3 = you have an array of 12 Flipkart product IDs. Use np.array_split() to divide this array 
into 5 nearly equal parts, and display each part.<br><br><em><strong>Hint:</strong> Check the shape
 of each split to confirm the division.</em>
 """

import numpy as np

product_ids = np.array([
    101, 102, 103, 104, 105, 106,
    107, 108, 109, 110, 111, 112
])

parts = np.array_split(product_ids, 5)

for part in parts:
    print(part)
    print("Shape:", part.shape)


"""task 4 =Simulate a WhatsApp group chat: create a 2D NumPy array where each row is a user and 
each column is the number of messages sent per day for a week. Use np.insert() to add a new user 
(row) with their message counts, then use np.delete() to remove the user who sent the least messages 
overall.
"""

import numpy as np

messages = np.array([
    [10, 12, 15, 8, 20, 18, 25],
    [5, 8, 6, 10, 12, 9, 7],
    [20, 18, 22, 25, 24, 30, 28]
])

# Add new user
new_user = np.array([15, 16, 14, 18, 20, 17, 19])

messages = np.insert(messages, 3, new_user, axis=0)

print("After adding new user:")
print(messages)

# Find user with least total messages
total = np.sum(messages, axis=1)
least_user = np.argmin(total)

# Delete that user
messages = np.delete(messages, least_user, axis=0)

print("After removing least active user:")
print(messages)

"""task 5 = Given a NumPy array of YouTube video view counts, use .view() to create a view and .
copy() to create a copy. Modify the first element in each and print all arrays to demonstrate the 
difference between view and copy.<br><br><em><strong>Hint:</strong> Observe which changes affect 
the original array.</em>
"""


import numpy as np

views = np.array([1000, 2000, 3000, 4000, 5000])

view_array = views.view()
copy_array = views.copy()

# Modify view
view_array[0] = 9999

# Modify copy
copy_array[0] = 8888

print("Original:", views)
print("View:", view_array)
print("Copy:", copy_array)