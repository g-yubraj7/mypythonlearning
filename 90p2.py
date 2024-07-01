Price = float(input("Price: "))
Discount = float(input("Discount: "))

final_price = f"The final price after discount is: Rs. {Price * (1 - Discount):.2f}"
print(f"{final_price}, Thank you for shopping with us.")