'''task 1 = Install pandas in your Python environment and create a Series named 'fav_cricket_teams' 
containing the names of your 5 favorite IPL teams. Print the Series.'''

import pandas as pd

fav_cricket_teams = pd.Series([
    "Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bengaluru",
    "Rajasthan Royals",
    "Kolkata Knight Riders"
])

print(fav_cricket_teams)




'''task 2 = Create a DataFrame named 'food_orders' with columns: 'Item', 'Restaurant', and 'Price'.
 Add 3 rows representing your last 3 Zomato or Swiggy orders and display the DataFrame.'''

import pandas as pd

food_orders = pd.DataFrame({
    "Item": ["Pizza", "Burger", "Biryani"],
    "Restaurant": ["Dominos", "McDonald's", "Behrouz"],
    "Price": [250, 150, 220]
})

print(food_orders)




'''task 3 = Given a list of follower counts for 5 Instagram influencers: [1200, 54000, 780, 150000, 32000],
 create a pandas Series called 'followers', then print the influencer(s) with the highest and 
lowest follower counts.<br><br><em><strong>Hint:</strong> Use Series.idxmax() and Series.idxmin() 
to find the indices.</em>'''

import pandas as pd

followers = pd.Series([1200, 54000, 780, 150000, 32000])

print("Highest followers:")
print(followers.idxmax(), followers.max())

print("Lowest followers:")
print(followers.idxmin(), followers.min())




'''task 4 = Create a DataFrame called 'playlist' with columns: 'Song', 'Artist', and 'Duration' 
(in minutes). Enter details for 4 songs you recently listened to on Spotify or YouTube Music, then 
print only the 'Song' and 'Duration' columns.'''


import pandas as pd

playlist = pd.DataFrame({
    "Song": ["Kesariya", "Heeriye", "Apna Bana Le", "Tum Hi Ho"],
    "Artist": ["Arijit Singh", "Jasleen Royal", "Arijit Singh", "Arijit Singh"],
    "Duration": [4.3, 3.2, 4.1, 4.2]
})

print(playlist[["Song", "Duration"]])