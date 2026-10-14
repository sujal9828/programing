'''task 1 = Load the 'IPL_2023_Batsmen.csv' dataset (containing player name, runs, matches, average,
 strike rate) into a Pandas DataFrame and display the first 10 rows.'''

import pandas as pd

df = pd.read_csv("IPL_2023_Batsmen.csv")

print(df.head(10))


'''task 2 = Perform univariate analysis on the 'runs' column: calculate and print the mean, median,
 mode, minimum, and maximum runs scored by batsmen in the IPL_2023_Batsmen dataset.'''

print("Mean:", df["runs"].mean())
print("Median:", df["runs"].median())
print("Mode:", df["runs"].mode()[0])
print("Minimum:", df["runs"].min())
print("Maximum:", df["runs"].max())



'''task 3 = Create a Pandas DataFrame for your top 5 favorite Zomato restaurants with columns: 
'name', 'rating', 'votes', and 'avg_cost'. Perform bivariate analysis between 'rating' and 'votes' 
by calculating their correlation coefficient.'''

import pandas as pd

data = {
    "name": ["Restaurant A", "Restaurant B", "Restaurant C",
             "Restaurant D", "Restaurant E"],
    "rating": [4.5, 4.0, 3.8, 4.7, 4.2],
    "votes": [500, 300, 200, 700, 400],
    "avg_cost": [500, 350, 250, 600, 400]
}

zomato = pd.DataFrame(data)

print(zomato)

correlation = zomato["rating"].corr(zomato["votes"])

print("Correlation:", correlation)



'''task 4 = Generate summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for all numeric 
columns in the IPL_2023_Batsmen DataFrame using the describe() function and interpret any one interesting
 insight you observe.<br><br><em><strong>Hint:</strong> Look for outliers or surprising averages 
 in the summary.</em>'''

import pandas as pd

df = pd.read_csv("IPL_2023_Batsmen.csv")

print(df.describe())


'''task 5 = Use ChatGPT to suggest two additional univariate or bivariate analyses you could perform 
on the IPL_2023_Batsmen dataset, then implement one of them in code and show the output.'''

top_batsman = df.loc[df["strike_rate"].idxmax()]

print("Batsman with highest strike rate:")
print(top_batsman[["player_name", "strike_rate"]])
