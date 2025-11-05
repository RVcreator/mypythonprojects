
password = input("Enter a password: ")

if len(password) < 8:
    print("Weak: password is too short (less than 8 characters).")
elif not any(ch.isdigit() for ch in password):
    print("Medium: add at least one digit.")
elif not any(ch.isupper() for ch in password):
    print("Medium: add an uppercase letter.")
elif not any(not ch.isalnum() for ch in password):
    print("Medium: add a special character (e.g. !, @, #, $).")
else:
    print("Strong password, good job!")
