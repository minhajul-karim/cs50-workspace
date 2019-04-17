import sys

# length = len(sys.argv)
# for i in range(length):

for i in sys.argv:
    print(i)

# Print all characters of command line arguments

for i in sys.argv:
    for c in i:
        print(c)