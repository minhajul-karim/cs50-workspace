#include <stdio.h>
#include <cs50.h>

// Prototypes
int digit_count(long long x);

int add_dig(int n);

void card_provider(long long card_num, int num_of_digits);

int validation(long long card_num, int digit_number);


int main()
{
    long long card_number;
    do
    {
        card_number = get_long_long("Number: ");
    }
    while (card_number <= 0);

    int number_of_dig = digit_count(card_number);

    int checksum = validation(card_number, number_of_dig);

    // Checking the card provider
    if (checksum == 2)
    {
        card_provider(card_number, number_of_dig);
    }
    else if (checksum == 3)
    {
        printf("INVALID\n");
    }
    return 0;
}


// Validation using Luhn Algorithm

int validation(long long card_num, int digit_number)
{
    long long p = 10, q = 1;
    int i, a, b, sum_of_multiplied_by_two = 0, sum_of_every_other_digits = 0, total;
    int last_lim_for_mul_by_two = digit_number / 2;


    // Sum of multiplying by 2
    for (i = 1; i <= last_lim_for_mul_by_two; i++)
    {
        a = (card_num / p) % 10;
        b = 2 * a;
        sum_of_multiplied_by_two += add_dig(b);
        p *= 100;
    }


    // Sum of every other digits those weren't mul by 2
    for (i = 1; i <= last_lim_for_mul_by_two + 1; i++)
    {
        a = (card_num / q) % 10;
        sum_of_every_other_digits += a;
        q *= 100;
    }

    // Total
    total = sum_of_multiplied_by_two + sum_of_every_other_digits;


    // Validation
    if (total % 10 == 0)
    {
        return 2;
    }
    else
    {
        return 3;
    }
}



// Function for digit count


int digit_count(long long x)
{
    int len = 1;
    if (x >= 10000000000000000)
    {
        len += 16;
        x /= 10000000000000000;
    }

    if (x >= 100000000)
    {
        len += 8;
        x /= 100000000;
    }

    if (x >= 10000)
    {
        len += 4;
        x /= 10000;
    }

    if (x >= 100)
    {
        len += 2;
        x /= 100;
    }

    if (x >= 10)
    {
        len += 1;
        x /= 10;
    }

    return len;
}

// Function to add digits together

int add_dig(int number)
{
    int sum = 0;

    while (number != 0)
    {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

// Check the card provider
void card_provider(long long card_num, int num_of_digits)
{
    long long first_one_dig = 0, first_two_dig = 0;
    if (num_of_digits == 13)
    {
        first_one_dig = card_num / 1000000000000;
        first_two_dig = card_num / 100000000000;
    }
    else if (num_of_digits == 15)
    {
        first_two_dig = card_num / 10000000000000;
    }
    else if (num_of_digits == 16)
    {
        first_one_dig = card_num / 1000000000000000;
        first_two_dig = card_num / 100000000000000;
    }

    if (num_of_digits == 15 && (first_two_dig == 34 || first_two_dig == 37))
    {
        printf("AMEX\n");
    }
    if ((num_of_digits == 13 || num_of_digits == 16) && first_one_dig == 4)
    {
        printf("VISA\n");
    }
    else if (num_of_digits == 16 && (first_two_dig == 51 || first_two_dig == 52 || first_two_dig == 53 || first_two_dig == 54 || first_two_dig == 55))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}