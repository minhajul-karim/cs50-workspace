#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int foo(int a);

int main()
{
    int a = 10;
    unsigned int b = foo(a);
    printf("b = %u\n", b);
}

unsigned int foo(int a)
{
    return a;
}