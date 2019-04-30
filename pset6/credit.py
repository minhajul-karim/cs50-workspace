from cs50 import get_int

# Main function
def main():
    # Input validation
    while True:
        card = get_int("Number: ")
        if (card > 0):
            break

    number_of_digits = len(str(card))
    checksum = validation(card, number_of_digits)

    if checksum == 0:
        # First few digits
        first_dig = int(str(card)[:1])
        first_two_dig = int(str(card)[:2])

        # Check the initial digits
        if first_dig == 4:
            print("VISA")

        elif (first_two_dig == 34 or first_two_dig == 37):
            print("AMEX")

        elif (first_two_dig == 51 or first_two_dig == 52 or first_two_dig == 53 or first_two_dig == 54 or first_two_dig == 55):
            print("MASTERCARD")
    else:
        print("INVALID")


# Validation function
def validation(card, digits):
    divisor_1, divisor_2 = 10, 1
    limit = digits // 2
    sum_of_multiplied_by_two, sum_of_every_other_digits = 0, 0

    # Sum of every other digits
    for i in range(limit):
        last_dig = (card // divisor_1) % 10
        multiplication = last_dig * 2
        sum_of_multiplied_by_two += sum(map(int, str(multiplication)))
        divisor_1 *= 100

    # Sum of other digits those weren't multiplied by 2
    for i in range(limit + 1):
        last_dig = (card // divisor_2) % 10
        sum_of_every_other_digits += last_dig
        divisor_2 *= 100

    return ((sum_of_multiplied_by_two + sum_of_every_other_digits) % 10)


# Call main
if __name__ == "__main__":
    main()