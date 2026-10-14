'''task 1 = Download a CSV file containing a list of movies with columns like 'title', 'genre', 
'rating', and 'box_office', then use pandas to load this file and select only the 'title' and 
'rating' columns using the loc method.'''

import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

print(df.columns)

print(df.loc[:, ['Series_Title', 'IMDB_Rating']])


'''task 2 = Given a DataFrame of Flipkart products with columns 'product_name', 'category', and 'price',
 use iloc to select the first 10 rows and all columns, and print the result.'''


import pandas as pd

df = pd.DataFrame({
    'product_name': ['Phone', 'Laptop', 'Mouse', 'Keyboard', 'Tablet',
                     'Monitor', 'Charger', 'Headphones', 'Watch', 'Speaker'],
    'category': ['Electronics'] * 10,
    'price': [15000, 45000, 500, 1200, 20000,
              12000, 800, 1500, 3000, 2500]
})

print(df.iloc[0:10, :])



'''task 3 = Using a DataFrame of food orders from Zomato with columns 'restaurant', 'order_amount', 
and 'delivery_time', filter and display only those orders where 'order_amount' is greater than 500 
using a boolean condition.'''

import pandas as pd

df = pd.DataFrame({
    'restaurant': ['A', 'B', 'C', 'D'],
    'order_amount': [300, 700, 450, 900],
    'delivery_time': [20, 30, 25, 40]
})

print(df[df['order_amount'] > 500])


'''task 4 =Given a DataFrame of Spotify songs with columns 'song', 'artist', 'streams', and 'duration', 
use the query() method to select all songs with more than 1,000,000 streams and duration less than 180 
seconds.<br><br><em><strong>Hint:</strong> Use the query syntax: query('streams > 1000000 and duration < 180')</em>'''

import pandas as pd

df = pd.DataFrame({
    'song': ['Song A', 'Song B', 'Song C'],
    'artist': ['Artist A', 'Artist B', 'Artist C'],
    'streams': [1500000, 800000, 2000000],
    'duration': [160, 200, 170]
})

result = df.query('streams > 1000000 and duration < 180')

print(result)


'''task 5 = Suppose you have a DataFrame of IPL cricket matches with columns 'team1', 'team2', 'winner', and 
'total_runs'. Write code to filter and display all matches where 'total_runs' is between 180 and 
220 using boolean indexing.<br><br><em><strong>Constraint:</strong> Do not use the query() method 
for this task.</em>'''

import pandas as pd

df = pd.DataFrame({
    'team1': ['CSK', 'MI', 'RCB', 'KKR'],
    'team2': ['MI', 'RCB', 'KKR', 'CSK'],
    'winner': ['CSK', 'MI', 'RCB', 'KKR'],
    'total_runs': [190, 150, 220, 230]
})

result = df[(df['total_runs'] >= 180) & (df['total_runs'] <= 220)]

print(result)