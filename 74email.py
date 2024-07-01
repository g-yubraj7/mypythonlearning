def format_email(email_address):
    """Parses and validates an email address."""

    # 1. Split the email into parts
    try:
        username, domain = email_address.split("@")
    except ValueError:
        return "Invalid email: Missing '@' symbol."

    # 2. Validate the username
    if not all(c.isalnum() or c == "." for c in username):
        return "Invalid email: Username must contain only letters, numbers, and periods '.'."

    # 3. Validate the domain
    if "." not in domain:
        return "Invalid email: Domain must contain a period '.'."

    return {"username": username, "domain": domain}  # Return the parsed parts


# Get user input
email = input("Enter an email address: ")

# Format and validate the email
result = format_email(email)

# Display the results
if isinstance(result, str):  # If result is an error message
    print(result)
else:
    print("Username:", result["username"])
    print("Domain:", result["domain"])