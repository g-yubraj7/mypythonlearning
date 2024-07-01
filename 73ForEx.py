print("Choose Base Currency:\n1. GBP\n2. NPR\n3. USD")
User_choice = int(input("Please enter your base currency: "))
if User_choice == 1:
    InGBP = float(input(f"Enter currency value in GBP: "))
    InNPR = InGBP * 169
    InUSD = InGBP * 1.27
    print(f"GBP {InGBP: .2f}:\n= Rs.{InNPR: .2f}\n= ${InUSD: .2f}")
elif User_choice == 2:
    InNPR = float(input(f"Enter currency value in NPR: "))
    InGBP = InNPR / 169
    InUSD = InNPR / 134
    print(f"NPR {InNPR: .2f}:\n= £{InGBP: .2f}\n= ${InUSD: .2f}")
elif User_choice == 3:
    InUSD = float(input(f"Enter currency value in USD: "))
    InGBP = InUSD / 1.27
    InNPR = InUSD * 134
    print(f"USD {InUSD: .2f}:\n= £{InGBP: .2f}\n= Rs.{InNPR: .2f}")
else :
    print("Please choose from 1-3")