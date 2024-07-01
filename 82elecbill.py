elecexp = {
    'January': 500,
    'February': 700,
    'March': 800,
    'April': 900,
    'May': 400,
    'June': 300,
    'July': 800,
    'August': 500,
    'September': 900,
    'October': 1200,
    'November': 900,
    'December': 600,
}
total = sum(elecexp.values())
print(f"May electricity bill is: {elecexp['May']}")
print(f"Total: {total}")
totalexp = print(f"Total exp is: {sum(elecexp.values())}")
Avgexp = print(f"Average electric expense is: {sum(elecexp.values())/12: .2f} ")
