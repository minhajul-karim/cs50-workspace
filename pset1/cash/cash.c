#include <stdio.h>
#include <cs50.h>
#include <math.h>


int main()
{
    int cents, count = 0, division = 0;
    double n, hundred = 100.00;

    //validating input
    do
    {
        n = get_float("Change owed: ");
    }
    while (n < 0);


    // Converting the dollar into cents
    cents = round(n * 100);

    //calculating how many 25c, 10c, 5c and 1c cents can be provided.
    //If cents is divisible by (25,10,5,1), we divide it to make it smaller and count the number of time it is divisible.

    if (cents >= 25)
    {
        division = cents / 25;
        cents = cents - (division * 25);
        count += division;
    }

    if (cents >= 10)
    {
        division = cents / 10;
        cents = cents - (division * 10);
        count += division;
    }

    if (cents >= 5)
    {
        division = cents / 5;
        cents = cents - (division * 5);
        count += division;
    }

    if (cents >= 1)
    {
        division = cents / 1;
        cents = cents - (division * 1);
        count += division;
    }

    printf("%d\n", count);
}