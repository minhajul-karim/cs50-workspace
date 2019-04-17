#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a, b;
    eprintf("a and b will be scanned now\n");
    a = get_int("a: ");
    b = get_int("b: ");
    eprintf("the result of addition of a and b will be done now\n");
    printf("res = %d\n", a + b);
    eprintf("The subtraction of a and b will be done now\n");
    printf("res = %d\n", a - b);
}