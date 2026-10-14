'''task 1 = Download a CSV file of IPL cricket players with columns for player name, team, and age,
 then use pandas to load it and print out all rows where the age column has missing values.'''

import pandas as pd

df = pd.read_csv("ipl_players.csv")

print(df[df["age"].isna()])



'''task 2 = Using a dataset of food delivery orders (with columns: order_id, customer_name, 
delivery_rating), use pandas to drop all rows where the delivery_rating is missing and display the 
cleaned DataFrame.'''

import pandas as pd

df = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_name": ["Aman", "Riya", "Rahul", "Neha"],
    "delivery_rating": [5, None, 4, None]
})

cleaned_df = df.dropna(subset=["delivery_rating"])

print(cleaned_df)




'''task 3 = Given a Flipkart-style product reviews dataset with some missing 'rating' values, use 
pandas to fill all missing ratings with the mean rating of the dataset and print the updated 
DataFrame.<br><br><em><strong>Hint:</strong> Use the fillna() method with the mean() function.
</em>'''

import pandas as pd

df = pd.DataFrame({
    "product_name": ["Mobile", "Laptop", "Headphones", "Watch"],
    "rating": [4, 5, None, 3]
})

df["rating"] = df["rating"].fillna(df["rating"].mean())

print(df)



'''task 4 = You have a Spotify playlist CSV with missing 'duration' values for some songs. Replace 
all missing durations with the median duration of the available songs using pandas, then save the 
cleaned DataFrame to a new CSV file.'''

import pandas as pd

df = pd.DataFrame({
    "song": ["Song A", "Song B", "Song C", "Song D"],
    "duration": [180, 240, None, 300]
})

df["duration"] = df["duration"].fillna(df["duration"].median())

df.to_csv("spotify_cleaned.csv", index=False)

print(df)



'''task 5 = Use ChatGPT to generate pandas code that replaces all missing values in a 'followers' 
column (from a simulated Instagram user data CSV) with 0, then test the code on your own sample 
data and submit both the code and the result.<br><br><em><strong>Hint:</strong> Ask ChatGPT: 
'How do I replace missing values in a pandas DataFrame column with zero?'</em>'''

import pandas as pd

df = pd.DataFrame({
    "username": ["aman", "riya", "rahul", "neha"],
    "followers": [1200, None, 850, None]
})

df["followers"] = df["followers"].fillna(0)

print(df)