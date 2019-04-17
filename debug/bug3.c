#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int score = get_int("Enter your mark: ");
    int tenth = (score / 10) * 10;
    char grade;

    switch(tenth)
    {
        case 100:
            grade = 'A';
        case 50:
            grade = 'D';
        case 30:
            grade = 'F';
    }
    printf("Your grade is %c\n", grade);
}