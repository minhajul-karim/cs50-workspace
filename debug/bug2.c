#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("x: ");
    if(x == 1)
    {
        printf("Hi\n");
    }
    else
    {
        printf("Hello\n");
    }
}