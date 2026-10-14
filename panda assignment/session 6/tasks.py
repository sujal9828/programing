'''task 1 = Load a CSV file of Spotify song streams (with columns: song, artist, streams, date) 
into a pandas DataFrame and use drop_duplicates() to remove any duplicate song entries, keeping only
 the first occurrence.'''

import pandas as pd

df = pd.read_csv("spotify.csv")

print("Original Data:")
print(df)

df = df.drop_duplicates(subset="song", keep="first")

print("\nAfter Removing Duplicates:")
print(df)



'''task 2 = Given a pandas DataFrame of Flipkart product reviews with columns: product_id, user_id,
 rating, review_text, identify and print the number of duplicate reviews (where product_id and
   user_id are both the same) before and after using drop_duplicates().'''

import pandas as pd

df = pd.DataFrame({
    "product_id": [101, 102, 101, 103, 102, 101],
    "user_id": [1, 2, 1, 3, 2, 4],
    "rating": [5, 4, 5, 3, 4, 2],
    "review_text": ["Good", "Nice", "Good", "Average", "Nice", "Okay"]
})

print("Before Removing Duplicates:")
print(df.duplicated(subset=["product_id", "user_id"]).sum())

df = df.drop_duplicates(subset=["product_id", "user_id"])

print("\nAfter Removing Duplicates:")
print(df.duplicated(subset=["product_id", "user_id"]).sum())

print("\nCleaned DataFrame:")
print(df)


'''task 3 = Use the IQR method to detect outliers in the 'order_amount' column of a Zomato orders 
DataFrame and print the order IDs that are considered outliers.<br><br><em><strong>Hint:</strong>
 Calculate Q1, Q3, and IQR, then filter orders outside the [Q1 - 1.5*IQR, Q3 + 1.5*IQR] range.</em>'''

import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "order_amount": [200, 250, 300, 280, 350, 400, 2000]
})

Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["order_amount"] < lower) |
    (df["order_amount"] > upper)
]

print("Outlier Order IDs:")
print(outliers["order_id"])


'''task 4 = For a DataFrame containing daily IPL match ticket sales (columns: date, tickets_sold),
 calculate the Z-score for each day's tickets_sold, and print the dates where the absolute Z-score 
 is greater than 2.<br><br><em><strong>Constraint:</strong> Use pandas and scipy.stats.zscore for
   calculations.</em>'''

import pandas as pd
from scipy.stats import zscore

df = pd.DataFrame({
    "date": [
        "2026-04-01",
        "2026-04-02",
        "2026-04-03",
        "2026-04-04",
        "2026-04-05",
        "2026-04-06"
    ],
    "tickets_sold": [100, 120, 110, 130, 115, 500]
})

df["z_score"] = zscore(df["tickets_sold"])

outliers = df[abs(df["z_score"]) > 2]

print("Outlier Dates:")
print(outliers["date"])


'''task 5 = Use ChatGPT or Copilot to generate a pandas function that finds and returns all outlier
 transaction amounts in a Paytm wallet DataFrame using the Z-score method, then test the function
   with sample data.'''

import pandas as pd
from scipy.stats import zscore

def find_outliers(df):
    df["z_score"] = zscore(df["amount"])
    result = df[abs(df["z_score"]) > 2]
    return result

df = pd.read_csv("paytm_wallet_transactions.csv")

outliers = find_outliers(df)

print(outliers)