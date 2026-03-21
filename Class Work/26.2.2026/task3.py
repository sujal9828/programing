day = int(input("enter day :"))
month = int(input("enter month :"))
year = int(input("enter year :"))

cday = 26
cmonth = 2
cyear = 2026
totalmonth = 12
rday = day - cday

print("year are :", cyear-year)
print("month are :",(totalmonth-month)+cmonth)
print("days are :", cday+rday)