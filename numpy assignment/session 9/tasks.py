"""task 1 = Create a NumPy array named prices with these values: [299, 499, 799, 0, 1599, -1, 899].
 Print the array and its data type.
 """

import numpy as np

prices = np.array([299, 499, 799, 0, 1599, -1, 899])

print("Prices:", prices)
print("Data Type:", prices.dtype)


"""task 2 =Some entries in the prices array are invalid (0 or negative). Replace all values less 
than or equal to zero with the average of the remaining positive prices.<br><br><em><strong>Hint:
</strong> Use boolean indexing and the mean() function.</em>
"""

positive_prices = prices[prices > 0]

average_price = np.mean(positive_prices)

prices[prices <= 0] = average_price

print("Cleaned Prices:", prices)


"""task 3 = Suppose you have a NumPy array quantities = [2, 1, 3, 4, 2, 1, 5]. Calculate the total b
ill for each item by multiplying the cleaned prices array with quantities, and print the resulting 
array
"""

quantities = np.array([2, 1, 3, 4, 2, 1, 5])

total_bill = prices * quantities

print("Bill for each item:", total_bill)


"""task 4 = Generate and print a summary report: show the minimum, maximum, average, and total of 
the cleaned prices array, and also the total bill for all items combined.<br><br><em><strong>Hint:
</strong> Use NumPy functions like min(), max(), mean(), and sum().</em>
"""


print("Minimum Price:", np.min(prices))
print("Maximum Price:", np.max(prices))
print("Average Price:", np.mean(prices))
print("Total Prices:", np.sum(prices))
print("Total Bill:", np.sum(total_bill))


"""task 5 = Use ChatGPT or Copilot to suggest a NumPy function or method that can help you find 
out how many unique price values are present in your cleaned prices array. Try the suggested method
and print the result.
"""

unique_prices = np.unique(prices)

print("Unique Prices:", unique_prices)
print("Number of Unique Prices:", len(unique_prices))