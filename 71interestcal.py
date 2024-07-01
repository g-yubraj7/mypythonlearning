Principal = float(input("Please enter the principal amount: "))
RateY = float(input("Please enter the annual rate of interest (in whole number): "))
TimeM = float(input("Please enter the time in month: "))

RatePercent = RateY/100
TimeY = TimeM/12

Simple_Interest = Principal * RatePercent * TimeY

print(f"Your Simple Interest Amount is: {Simple_Interest: .2f}, given the principal amount of {Principal: .2f}, rate of interest of {RateY: .2f}% and time period of {TimeY} years.")