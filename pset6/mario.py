from cs50 import get_int

# Validating input
while True:
    height = get_int("Height: ")
    if (height > 0 and height <= 8):
        break

space = height - 1
star = 1

for i in range(height):
    # Left side
    print(" " * space, end="")
    space -= 1
    print("#" * star, end="")
    star += 1

    # Spaces - Middle side
    print(" " * 2, end="")

    # Right side
    print("#" * (i + 1))