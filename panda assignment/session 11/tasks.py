'''task 1 = Use pd.concat to combine two DataFrames representing January and February orders from a
 Swiggy-style food delivery app, stacking them row-wise to create a single DataFrame with all orders.'''

import pandas as pd

jan_orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer': ['Amit', 'Rahul', 'Priya'],
    'amount': [250, 400, 300]
})

feb_orders = pd.DataFrame({
    'order_id': [104, 105, 106],
    'customer': ['Neha', 'Ravi', 'Simran'],
    'amount': [350, 500, 200]
})

all_orders = pd.concat([jan_orders, feb_orders], ignore_index=True)

print(all_orders)


'''task 2 = Given two DataFrames — one with Flipkart product details and another with their respective
 ratings — use pd.concat to merge them column-wise so each product row includes its rating.'''

import pandas as pd

products = pd.DataFrame({
    'product': ['Mobile', 'Laptop', 'Headphones'],
    'price': [15000, 50000, 2000]
})

ratings = pd.DataFrame({
    'rating': [4.5, 4.7, 4.2]
})

result = pd.concat([products, ratings], axis=1)

print(result)


'''task 3 = Create a DataFrame showing daily song streams for three users on Spotify for one week, 
then use the pivot function to reshape the data so each row is a user and each column is a day.'''

import pandas as pd

df = pd.DataFrame({
    'user': ['Amit', 'Amit', 'Amit', 'Rahul', 'Rahul', 'Rahul',
             'Priya', 'Priya', 'Priya'],
    'day': ['Monday', 'Tuesday', 'Wednesday',
            'Monday', 'Tuesday', 'Wednesday',
            'Monday', 'Tuesday', 'Wednesday'],
    'streams': [100, 150, 120, 200, 180, 220, 90, 110, 130]
})

result = df.pivot(index='user', columns='day', values='streams')

print(result)

'''task 4 = Given a DataFrame of Zomato restaurant orders (with columns: restaurant, month, 
total_amount), use pivot_table to calculate the average order amount per restaurant for each
 month.'''

import pandas as pd

df = pd.DataFrame({
    'restaurant': ['Pizza Hut', 'Dominos', 'Pizza Hut',
                   'Dominos', 'Pizza Hut', 'Dominos'],
    'month': ['January', 'January', 'February',
              'February', 'January', 'January'],
    'total_amount': [500, 600, 700, 800, 300, 400]
})

result = df.pivot_table(
    index='restaurant',
    columns='month',
    values='total_amount',
    aggfunc='mean'
)

print(result)

'''task 5 = Download three monthly sales CSV files for a mock Myntra store (e.g., sales_jan.csv, 
sales_feb.csv, sales_mar.csv), then use pd.concat to combine them into one DataFrame and display 
the total sales per product.<br><br><em><strong>Hint:</strong> Use groupby on the product column 
after concatenation to sum sales.</em>'''

import pandas as pd

jan = pd.DataFrame({
    'product': ['Shirt', 'Jeans', 'Shoes'],
    'sales': [5000, 8000, 10000]
})

feb = pd.DataFrame({
    'product': ['Shirt', 'Jeans', 'Shoes'],
    'sales': [6000, 7000, 12000]
})

mar = pd.DataFrame({
    'product': ['Shirt', 'Jeans', 'Shoes'],
    'sales': [7000, 9000, 11000]
})

jan.to_csv('sales_jan.csv', index=False)
feb.to_csv('sales_feb.csv', index=False)
mar.to_csv('sales_mar.csv', index=False)

