from cs50 import get_string

name = get_string("Name: ");
initials = ""

# Iterates through every character of name
for i in name:
    # If i, a single charactered str of name is uppercase append it to initials
    if i.isupper():
        initials += i

print(initials)