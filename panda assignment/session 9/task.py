'''task 1 = Create a Pandas Series of 5 random date strings in the format 'DD-MM-YYYY', then convert
 this Series to datetime objects using pd.to_datetime and print the result.'''

import pandas as pd

dates = pd.Series([
    '15-01-2025',
    '22-03-2025',
    '10-06-2025',
    '05-08-2025',
    '14-12-2025'
])

dates = pd.to_datetime(dates, format='%d-%m-%Y')

print(dates)


'''task 2 = Given a DataFrame with a 'release_date' column containing movie release dates (as strings),
add three new columns: 'year', 'month', and 'day' by extracting these values from the 'release_date'
 column using Pandas.<br><br><em><strong>Hint:</strong> Use the .dt accessor after converting to 
 datetime.</em>'''

import pandas as pd

df = pd.DataFrame({
    'movie': ['Movie A', 'Movie B', 'Movie C'],
    'release_date': ['15-01-2024', '20-06-2023', '10-12-2025']
})

df['release_date'] = pd.to_datetime(
    df['release_date'], format='%d-%m-%Y'
)

df['year'] = df['release_date'].dt.year
df['month'] = df['release_date'].dt.month
df['day'] = df['release_date'].dt.day

print(df)


'''task 3 = Generate a date range for the next 7 days starting from today using pd.date_range, and 
display the list of dates in the console.'''

import pandas as pd

dates = pd.date_range(start=pd.Timestamp.today().normalize(), periods=7)

print(dates)

'''task 4 = Suppose you have a DataFrame of Zomato Gold subscriptions with columns 'user_id' and 
'start_date' (as strings). Calculate the tenure (in days) for each user by subtracting the 
'start_date' from today's date, and add it as a new column 'tenure_days'.<br><br><em><strong>Hint:
</strong> Use pd.to_datetime for conversion and (today - start_date).dt.days for calculation.</em>'''

import pandas as pd

df = pd.DataFrame({
    'user_id': [101, 102, 103],
    'start_date': ['01-01-2026', '15-05-2026', '01-09-2026']
})

df['start_date'] = pd.to_datetime(
    df['start_date'], format='%d-%m-%Y'
)

today = pd.Timestamp.today().normalize()

df['tenure_days'] = (today - df['start_date']).dt.days

print(df)
