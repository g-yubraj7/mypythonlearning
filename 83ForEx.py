NEP = float(input("Enter Nepalese Rs. "))

USD = NEP/134
JPN = NEP*1.2
EUR = NEP/140
GBP = NEP/170

print(f"USD for Rs.{NEP} is ${USD: .2F}")
print(f"JPN for Rs.{NEP} is {JPN: .2F}")
print(f"EUR for Rs.{NEP} is {EUR: .2F}")
print(f"GBP for Rs.{NEP} is {GBP: .2F}")