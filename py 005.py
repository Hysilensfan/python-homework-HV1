s = int(input());print(f"{s//(24*60**2)}D{s%(24*60**2)//60**2}H{s%(24*60**2)%(60**2)//60}M{s%(24*60**2)%(60**2)%60}S") #hint:1day24hour;1hour60minute;1minute60second;1day=24x60x60=86400second
