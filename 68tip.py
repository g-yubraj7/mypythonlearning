bill_total = float(input("Enter the bill amount: "))
tip_percent = int(input("Enter the tip% (in whole number): "))

tip_amount = float(bill_total*tip_percent/100)

print(f"At Rs.{bill_total: .2f} bill amount, your tip amount is:{tip_amount: .2f}, based on tip % of {tip_percent}%.")
