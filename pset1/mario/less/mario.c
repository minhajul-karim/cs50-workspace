#include <stdio.h>
#include <cs50.h>

int main()
{
    int n, i, j, k, space_ends, star_starts;


    // Validating input
    do
    {
        n = get_int("Height: ");

    }
    while (n < 0 || n > 23);

    space_ends = n - 1;
    star_starts = space_ends + 1;

    ///printing spaces and starts
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= space_ends; j++)
        {
            printf(" ");
        }

        space_ends--;

        for (k = star_starts; k <= n + 1; k++)
        {
            printf("#");
        }

        star_starts--;
        printf("\n");
    }

}
