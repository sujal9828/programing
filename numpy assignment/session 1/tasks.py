''' Task 1 = Install NumPy using pip and write a Python script list_vs_array.py 
 that creates a list and a NumPy array, each containing the numbers from 1 to 1000.
'''

import numpy as np

list1 = list(range(1, 1001))
array1 = np.array(range(1, 1001))

print(list1)
print(array1)


'''Task 2 = In your script, measure and print the memory usage (in bytes) of both the Python list 
 and the NumPy array containing 1000 integers.<br><br><em><strong>Hint:</strong> 
 Use the sys.getsizeof() function for the list and the nbytes attribute for the NumPy array.</em>
'''
import sys

print("List memory:", sys.getsizeof(list1), "bytes")
print("Array memory:", array1.nbytes, "bytes")


'''
Task 3 = Write a function compare_addition_speed() that adds 5 to every element in both a 
Python list and a NumPy array of 10,000 integers, and prints the time taken for each.
<br><br><em><strong>Hint:</strong> Use the time module to measure execution time.</em>
'''
import numpy as np
import time

list1 = list(range(10000))
array1 = np.array(range(10000))

#list
start = time.time()
for i in range(10000):
    list1[i] = list1[i] + 5

end = time.time()
print("List time:", end - start)

#numpy array
start = time.time()
array1 = array1 + 5
end = time.time()
print("Array time:", end - start)


'''
Task 4 = Explain with code how vectorized operations in NumPy can replace for-loops when
multiplying all elements of an array by 2. Show both the loop and the vectorized version
using a Zomato-style example: multiplying all restaurant ratings by 2.
'''

ratings = [3.5, 4, 4.5, 3]

new_ratings = []

for x in ratings:
    new_ratings.append(x * 2)

print(new_ratings)

# In list we have to use loop

import numpy as np

ratings = np.array([3.5, 4, 4.5, 3])

print(ratings * 2)

# In numpy we can multiply all array elements by 2 without using a loop.
