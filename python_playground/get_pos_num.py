from cs50 import get_int

def main():
    x = get_pos_int("Enter a positive number: ");
    print(x)

def get_pos_int(prompt):
    while True:
        n = get_int(prompt)
        if n > 0:
            return n

if __name__ == "__main__":
    main()