
print("1. KM\n2. Miles\n3. Meters")
User_Choice = int(input("Please choose from which basis you want to convert: "))

if User_Choice == 1:
    InKM = float(input("Please enter the distance in KM: "))
    InMiles = InKM/1.609
    InMeters = InKM*1000
    print(f"{InKM} kilometers = {InMiles: .2f} miles\n{InKM} kilometers = {InMeters: .2f} meters")
elif User_Choice==2:
    InMiles = float(input("Please enter the distance in Miles: "))
    InKM = InMiles*1.609
    InMeters = InMiles*1609.34
    print(f"{InMiles} miles = {InKM: .2f} kilometers\n{InMiles} miles = {InMeters: .2f} meters")
else:
    InMeters = float(input("Please enter the distance in meters: "))
    InKM = InMeters/1000
    InMiles = InMeters/1609.34
    print(f"{InMeters} meters = {InKM: .2f} kilometers\n{InMeters} meters = {InMiles: .2f} miles")



