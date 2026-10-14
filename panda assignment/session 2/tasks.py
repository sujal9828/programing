'''task 1 = Download a CSV file of IPL match results from Kaggle or any open dataset, then use pandas 
read_csv() to load it into a DataFrame and display the first 10 rows using head().'''

import pandas as pd

ipl = pd.read_csv("matches.csv")

print(ipl.head(10))


'''task 2 = Find a small Excel file of your own mobile expenses (or create one with 5-10 rows), 
then use pandas read_excel() to load it and print the last 3 rows using tail()'''

import pandas as pd

expenses = pd.read_excel("mobile_expenses.xlsx")

print(expenses.tail(3))



'''task 3 = Use describe() and info() on a DataFrame loaded from a Zomato restaurant dataset 
(or any food delivery data you can find online), and write down 2 insights about the data 
(for example: number of restaurants, missing values, or average ratings).<br><br><em><strong>Hint:</strong> 
Focus on what info() and describe() reveal about columns and data types.</em>'''


import pandas as pd

df = pd.read_csv("zomato.csv")

print(df.info())

print(df.describe())


'''task 4 = Export the DataFrame from your IPL or food delivery dataset to a new CSV file called 
'filtered_data.csv', but only include the first 20 rows.'''

import pandas as pd

ipl = pd.read_csv("matches.csv")

filtered_data = ipl.head(20)

filtered_data.to_csv("filtered_data.csv", index=False)

print("CSV file created successfully")



'''task 5 = Load any dataset of your choice (not the one used in the class demo), and export it to 
Excel format with a custom sheet name like 'Analysis2024'.<br><br><em><strong>Constraint:</strong>
Use the to_excel() method and set the sheet_name parameter.</em>'''

import pandas as pd

ipl = pd.read_csv("matches.csv")

ipl.to_excel(
    "ipl_analysis.xlsx",
    sheet_name="Analysis2024",
    index=False
)

print("Excel file created successfully")

