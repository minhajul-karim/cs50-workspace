from cs50 import get_int

def main():
    x = get_int("x: ")
    y = get_int("y: ")

    if x > y:
        print(f"{x} is larger than {y}");
    elif x < y:
        print(f"{x} is less than {y}");
    else:
        print(f"{x} and {y} are equal");

if __name__ == "__main__":
        main()