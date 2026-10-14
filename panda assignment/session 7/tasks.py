'''task 1 = Download a sample Flipkart-style product sales CSV with columns: ProductName, Price, 
Qty. Using pandas, add a new column called 'TotalValue' that multiplies Price and Qty for each row,
 then display the updated DataFrame.'''

import pandas as pd

data = {
    'ProductName': ['Mobile', 'Laptop', 'Headphones', 'Mouse'],
    'Price': [15000, 45000, 2000, 500],
    'Qty': [2, 1, 3, 4]
}

df = pd.DataFrame(data)

df['TotalValue'] = df['Price'] * df['Qty']

print(df)


'''task 2 = Given a DataFrame of food items with columns: Item, Price, and Qty, use the apply() 
function with a lambda to create a new column 'DiscountedPrice' that applies a 10% discount to the 
Price for each item.'''

import pandas as pd

data = {
    'Item': ['Pizza', 'Burger', 'Sandwich', 'Pasta'],
    'Price': [200, 150, 100, 250],
    'Qty': [2, 3, 1, 2]
}

df = pd.DataFrame(data)

df['DiscountedPrice'] = df['Price'].apply(lambda x: x * 0.90)

print(df)



'''task 3 = You have a DataFrame of Instagram posts with columns: PostID, Likes, and Comments. Use 
applymap() to convert all numeric values in the Likes and Comments columns to strings formatted as 
'1.5K', '2M', etc., similar to how Instagram displays large numbers.<br><br><em><strong>Hint:</strong> 
Write a helper function that takes a number and returns the formatted string, then use applymap() 
on the relevant columns.</em>'''

import pandas as pd

data = {
    'PostID': [101, 102, 103],
    'Likes': [1500, 2000000, 850],
    'Comments': [2500, 150000, 5000000]
}

df = pd.DataFrame(data)

def format_number(num):
    if num >= 1000000:
        return str(round(num / 1000000, 1)) + 'M'
    elif num >= 1000:
        return str(round(num / 1000, 1)) + 'K'
    else:
        return str(num)

df[['Likes', 'Comments']] = df[['Likes', 'Comments']].map(format_number)

print(df)



'''task 4 = Given a DataFrame of Zomato restaurant orders with columns: Restaurant, Price, Qty, 
and DeliveryCharge, use a lambda function with apply() to add a column 'FinalAmount' that calculates
the total amount for each order as (Price * Qty) + DeliveryCharge.'''

import pandas as pd

data = {
    'Restaurant': ['Dominos', 'McDonalds', 'Burger King'],
    'Price': [200, 150, 180],
    'Qty': [2, 3, 2],
    'DeliveryCharge': [30, 20, 25]
}

df = pd.DataFrame(data)

df['FinalAmount'] = df.apply(
    lambda x: (x['Price'] * x['Qty']) + x['DeliveryCharge'],
    axis=1
)

print(df)



'''task 5 = Use ChatGPT to generate a pandas code snippet that adds a column 'GST' to a DataFrame 
of Myntra orders, where GST is calculated as 5% of (Price * Qty). Paste the AI-generated code, run 
it, and write 2 lines about what you learned from the AI's explanation.'''

import pandas as pd

data = {
    'Product': ['Shirt', 'Jeans', 'Shoes'],
    'Price': [500, 1200, 2000],
    'Qty': [2, 1, 1]
}

df = pd.DataFrame(data)

df['GST'] = (df['Price'] * df['Qty']) * 0.05

print(df)