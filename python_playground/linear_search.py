from cs50 import get_string

phonebook = [
    "ammu",
    "abbu",
    "dadu",
    "fuppy"
]

name = get_string("Enter a name: ")
if name in phonebook:
    print(f"Calling {name}")
else:
    print("Not found")