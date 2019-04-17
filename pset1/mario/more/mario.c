#include <stdio.h>
#include <cs50.h>

int main()
{

    int n, i, j, k, p, q, space_ends, star_starts;


    // Validating input

    do
    {

        n = get_int("Height: ");

    }
    while (n < 0 || n > 23);

    space_ends = n - 1;
    star_starts = space_ends + 1;


    ///Building the left triangle

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= space_ends; j++)
        {
            printf(" ");
        }
        space_ends--;

        for (k = star_starts; k <= n; k++)
        {
            printf("#");
        }
        star_starts--;

        ///printing the middle 2 space

        printf("  ");

        ///Building the right triangle

        for (p = 1; p <= i; p++)
        {
            printf("#");
        }

        ///print the line break
        printf("\n");

    }

}