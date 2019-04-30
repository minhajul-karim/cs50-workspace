from cs50 import get_int

# Validating input
while True:
    height = get_int("Height: ")
    if (height > 0 and height <= 8):
        break;

space = height - 1
star = 1

for i in range(height):
    print(" " * space, end="")
    space -= 1
    print("#" * star)
    star += 1



# tests
# for i in range(height):
#     print("#")
# print("-" * 2, end="")
# print("*")