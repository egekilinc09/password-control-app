# Ask the user to enter a password
password = input("Please enter your password: ")

#List of required characters
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_chars = [".",",",":",";","!", "@", "#", "$", "%", "&", "/", "(", ")", "=", "?", "*", "+", "-", "_"]

# Keep the list of missing requirements
missing = []

# password must be at least 8 characters long
if len(password) < 8:
    missing.append("at least 8 characters")

# Password must include at least one digit
if not any(char in digits for char in password):
    missing.append("a digit")

# Password must include at least one letter
if not any(char in letters for char in password):
    missing.append("a capital letter")

# Password must include at least one special character
if not any(char in special_chars for char in password):
    missing.append("a special character")

# Final output based on validation
if not missing:
    print("Strong password.")
else:
    print("Weak password. Missing: " + ", ".join(missing))
