'''task 1 = Create a DataFrame named 'movies' with columns: 'title', 'rating', and 'release_year' 
for at least 6 popular Bollywood films. Use sort_values() to display the movies sorted by 'rating' 
from highest to lowest.'''

import pandas as pd

movies = pd.DataFrame({
    'title': ['3 Idiots', 'Dangal', 'Sholay', 'PK', '12th Fail', 'Lagaan'],
    'rating': [8.4, 8.3, 8.1, 8.1, 8.7, 8.1],
    'release_year': [2009, 2016, 1975, 2014, 2023, 2001]
})

result = movies.sort_values(by='rating', ascending=False)

print(result)



'''task 2 = Given a DataFrame of IPL teams with columns 'team', 'points', and 'net_run_rate', use 
sort_index() to sort the DataFrame by the default index in descending order, then print the result.
<br><br><em><strong>Hint:</strong> Use the ascending parameter in sort_index().</em>'''

import pandas as pd

ipl = pd.DataFrame({
    'team': ['CSK', 'MI', 'RCB', 'KKR'],
    'points': [17, 14, 12, 16],
    'net_run_rate': [0.5, 0.2, 0.1, 0.4]
})

result = ipl.sort_index(ascending=False)

print(result)


'''task 3 = Reset the index of a DataFrame containing a list of trending YouTube videos (columns: 
'video_title', 'views', 'likes'), and make sure the old index is not added as a column in the 
result.<br><br><em><strong>Constraint:</strong> Use the drop=True argument in reset_index().
</em>'''

import pandas as pd

youtube = pd.DataFrame({
    'video_title': ['Video A', 'Video B', 'Video C'],
    'views': [100000, 200000, 150000],
    'likes': [5000, 10000, 7500]
}, index=[10, 20, 30])

result = youtube.reset_index(drop=True)

print(result)



'''task 4 = You have a DataFrame of Zomato restaurant names and their ratings. Use reindex() to 
rearrange the rows so that your favorite restaurant appears first, followed by the rest in any 
order.'''

import pandas as pd

restaurants = pd.DataFrame({
    'restaurant': ['Dominos', 'Haldiram', 'Burger King', 'McDonalds'],
    'rating': [4.2, 4.0, 4.1, 4.3]
}, index=[0, 1, 2, 3])

result = restaurants.reindex([2, 0, 1, 3])

print(result)



'''task 5 = Take a DataFrame of Flipkart products with columns 'product_name', 'price', and 
'discount'. First, sort the products by 'discount' descending, then reset the index so it starts 
from 0 and is sequential after sorting'''


import pandas as pd

products = pd.DataFrame({
    'product_name': ['Shoes', 'Watch', 'Headphones', 'Bag'],
    'price': [2000, 1500, 3000, 1000],
    'discount': [20, 40, 15, 30]
})

result = products.sort_values(
    by='discount', ascending=False
).reset_index(drop=True)

print(result)