'''Task 1 = Create a NumPy array representing the number of likes on 7 Instagram posts 
and print its ndim, shape, size, dtype, itemsize, and nbytes properties.
'''
import numpy as np

likes = np.array([100, 250, 180, 300, 150, 400, 220])

print("ndim:", likes.ndim)
print("shape:", likes.shape)
print("size:", likes.size)
print("dtype:", likes.dtype)
print("itemsize:", likes.itemsize)
print("nbytes:", likes.nbytes)


'''Task 2 = Given a 2D NumPy array of daily step counts for 5 days (each row is a day, columns are
morning and evening), use reshape() to convert it into a 1D array,then back to a 2D array with 
5 rows and 2 columns.<br><br><em><strong>Hint:</strong>Use the shapeattribute to check your array 
after each reshape.</em>
'''
steps = np.array([
    [3000, 5000],
    [4000, 6000],
    [3500, 5500],
    [4500, 7000],
    [5000, 8000]
])

print("Original shape:", steps.shape)

one_d = steps.reshape(10)
print("1D:", one_d)
print("Shape:", one_d.shape)

two_d = one_d.reshape(5, 2)
print("2D:", two_d)
print("Shape:", two_d.shape)


'''Task 3 = Build a NumPy array representing the prices of 12 food items from a Zomato order,
then use ravel(), flatten(), and resize() to create different shaped versions of the data and 
print each result.<br><br><em><strong>Constraint:</strong> Show the difference between ravel() 
and flatten() in your code comments.</em>
'''
prices = np.array([
    [100, 200, 150, 300],
    [250, 120, 180, 220],
    [90, 160, 270, 130]
])

# ravel() → 1D array
# flatten() → 1D copy banata hai
# ravel() usually view deta hai, flatten() copy deta hai

print("Ravel:", prices.ravel())
print("Flatten:", prices.flatten())

prices.resize(4, 3)
print("Resize:")
print(prices)


'''Task 4 = Take a 3x3 NumPy array representing a mini Spotify playlist grid (rows: playlists, columns: song counts in categories like 
Pop, Rock, Indie). Use both T and np.transpose() to swap rows and columns, then print the transposed array.
'''
playlist = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [12, 22, 32]
])

print("Using T:")
print(playlist.T)

print("Using transpose:")
print(np.transpose(playlist))


'''Task 5 = Given a 1D NumPy array of 15 Flipkart product ratings, use reshape() to convert it into a 3x5 array, then use flatten() to 
return it to a 1D array. Explain in a comment when you would use flatten() versus ravel() in real projects.
'''

ratings = np.array([
    4, 5, 3, 4, 2,
    5, 4, 3, 5, 4,
    2, 3, 5, 4, 5
])

new_array = ratings.reshape(3, 5)

print("3 x 5:")
print(new_array)

back_to_1d = new_array.flatten()

print("1D:")
print(back_to_1d)

# flatten() → jab hume independent copy chahiye
# ravel() → jab sirf 1D form chahiye aur copy zaroori nahi