from cs50 import get_int

def main():
    x = get_int("Enter a number: ")
    res = square(x)
    print(f"{res}")

def square(number):
    """Returns the square of number"""
    return number**2

if __name__ == "__main__":
    main()