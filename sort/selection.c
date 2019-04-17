#include <stdio.h>

int main()
{
    int i, j, compared_val, sm, sm_index, n;

    //Getting the number of elements
    printf("Enter the number of elements\n");
    scanf("%d", &n);
    int a[n];

    //Getting the individual values
    printf("Enter the individual vlues\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    //Doing the sort
    for (i = 0; i < n; i++)
    {
        compared_val = a[i];
        for (j = i; j < n; j++)
        {
            if (a[j] <= compared_val)
            {
                compared_val = a[j];
                sm = a[j];
                sm_index = j;
            }
        }
        //swap
        a[sm_index] = a[i];
        a[i] = sm;
    }

    //print
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}