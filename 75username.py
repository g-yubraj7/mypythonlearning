def generate_username(first_name, last_name, favorite_number):
    """Generates a username based on user input."""

    # 1. Combine user information (You can customize this part!)
    username_base = last_name[0] + "_" + first_name[:3] + str(favorite_number)

    # 2. Ensure lowercase and remove spaces
    username = username_base.lower().replace(" ", "")

    # 3. Apply length restrictions (optional)
    if len(username) > 15:
        username = username[:15]
    elif len(username) < 6:
        username += "123"  # Add characters to meet minimum length

    return username

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_number = input("Enter your favorite number: ")

# Generate the username
username = generate_username(first_name, last_name, favorite_number)

print("Generated username:", username)