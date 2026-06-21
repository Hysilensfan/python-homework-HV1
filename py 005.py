s = int(input())
print(f"{s//(24*60**2)}D{s%(24*60**2)//60**2}H{s%(24*60**2)%(60**2)//60}M{s%(24*60**2)%(60**2)%60}S")
"""
1day=24hour
1hour=60minute
1minute=60second
1day=24hourx60minutex60second=86400second
"""
