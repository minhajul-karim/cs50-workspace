#include <stdio.h>

int main(void)
{
    int a[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    int n = 10, x = n - 2, i, j, temp, swap;

    for (i = 0; ; i++)
    {
        swap = 0;
        for (j = 0; j <= x; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swap++;
            }
        }
        x--;

        if (swap == 0)
        {
            printf("Sorted list: ");
            for (i = 0; i < n; i++)
            {
                printf("%d ", a[i]);
            }
            printf("\n");
            return 0;
        }
    }
    return 0;
}
