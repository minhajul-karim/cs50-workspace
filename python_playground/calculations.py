from cs50 import get_int

def main():
    x = get_int("X: ")
    y = get_int("Y: ")

    print(f"{x} + {y} = {x + y}");
    print(f"{x} - {y} = {x - y}");
    print(f"{x} * {y} = {x * y}");
    print(f"{x} / {y} = {x / y}");
    print(f"{x} // {y} = {x // y}");


if __name__ == "__main__":
    main()