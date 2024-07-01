def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
# Get Celsius temperature from the user
celsius = float(input("Enter temperature in Celsius: "))
# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)
# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")