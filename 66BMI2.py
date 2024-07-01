Height = float(input("Please enter your height in inches: "))
Weight = float(input("Please enter your weight in KG: "))
Height_met = Height*0.0254 

bmi = Weight/Height_met**2

# print(f"Your BMI is {bmi: .2f}")

if 18 <= bmi <= 25:
  print(f"Your BMI is: {bmi:.2f}, which indicates a healthy weight.")
elif bmi < 18:
  print(f"Your BMI is: {bmi:.2f}, which indicates underweight, please make food your friend.")
else:  # bmi > 25
  print(f"Your BMI is: {bmi:.2f}, which indicates overweight. please make food your enemy.")
