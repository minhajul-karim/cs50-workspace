from sys import argv, exit
from cs50 import get_string

# Check if user has provided any command line arg
if (len(argv) != 2):
    print("Usage: python caeser.py key")
    exit(1)

# Convert the command line arg into an int
key = int(argv[1])
#print(key)

plaintext = get_string("plaintext: ")

print("ciphertext: ", end="")

for c in plaintext:
    # if c is a letter
    if c.isalpha():
        # if c is an uppercase letter
        if c.isupper():
            base = ord(c) - 65 # 0,1,2
            index = (base + key) % 26 # new index
            new_char = chr(65 + index)
            print(new_char, end="")

        # if c is a lowercase letter
        else:
            base = ord(c) - 97 # 0,1,2
            index = (base + key) % 26 # new index
            new_char = chr(97 + index)
            print(new_char, end="")

    # if c is some other char
    else:
        print(c, end="")

print()
