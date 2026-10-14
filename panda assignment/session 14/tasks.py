'''task 1 = Download a publicly available CSV dataset of IPL cricket matches (for example, from 
Kaggle or data.world), and use pandas to load it into a DataFrame named ipl_df. Display the first 
5 rows.'''

import pandas as pd
import numpy as np

ipl_df = pd.read_csv("matches.csv")

print(ipl_df.head())


'''task 2 = Clean the ipl_df DataFrame by removing any rows where the 'winner' column is missing or 
null, and reset the index afterwards.'''

ipl_df = ipl_df.dropna(subset=["winner"])

ipl_df = ipl_df.reset_index(drop=True)

print(ipl_df.head())


'''task 3 = Transform the ipl_df DataFrame to add a new column 'match_margin_type' that labels each
match as 'Runs' if the 'win_by_runs' value is greater than 0, 'Wickets' if 'win_by_wickets' is 
greater than 0, or 'Tie/No Result' otherwise.<br><br><em><strong>Hint:</strong> Use numpy.select()
or pandas' apply() for this transformation.</em>'''

conditions = [
    ipl_df["win_by_runs"] > 0,
    ipl_df["win_by_wickets"] > 0
]

choices = ["Runs", "Wickets"]

ipl_df["match_margin_type"] = np.select(
    conditions,
    choices,
    default="Tie/No Result"
)

print(ipl_df[["winner", "win_by_runs",
"win_by_wickets", "match_margin_type"]].head())


'''task 4 = Merge the ipl_df DataFrame with a separate DataFrame containing IPL team names and their
 home cities (create this manually with at least 5 teams), using the team name as the key, and add 
 the home city for both 'team1' and 'team2' in each match.'''

teams = pd.DataFrame({
    "team": [
        "Mumbai Indians",
        "Chennai Super Kings",
        "Royal Challengers Bangalore",
        "Kolkata Knight Riders",
        "Rajasthan Royals"
    ],
    "home_city": [
        "Mumbai",
        "Chennai",
        "Bengaluru",
        "Kolkata",
        "Jaipur"
    ]
})

ipl_df = ipl_df.merge(
    teams.rename(columns={
        "team": "team1",
        "home_city": "team1_home_city"
    }),
    on="team1",
    how="left"
)

ipl_df = ipl_df.merge(
    teams.rename(columns={
        "team": "team2",
        "home_city": "team2_home_city"
    }),
    on="team2",
    how="left"
)

print(ipl_df[[
    "team1", "team1_home_city",
    "team2", "team2_home_city"
]].head())



'''task 5 = Create a pivot table to show the total number of matches won by each team per season, 
and display the top 3 teams with the most wins in any single season.'''


pivot = pd.pivot_table(
    ipl_df,
    index="season",
    columns="winner",
    values="id",
    aggfunc="count",
    fill_value=0
)

print("Matches won by each team per season:")
print(pivot)

top3 = pivot.stack().reset_index()
top3.columns = ["season", "team", "wins"]

top3 = top3.sort_values(
    by="wins",
    ascending=False
).head(3)

print("\nTop 3 teams with most wins in a single season:")
print(top3)