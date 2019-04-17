// Helper functions for music

#include <cs50.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include "helpers.h"

int calculation(char accidental, int octave_int, int n);

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int res = 0;
    int a = atoi(&fraction[0]);
    int b = atoi(&fraction[2]);
    //printf("a = %d, b = %d\n", a, b);
    res = (a * 8) / b;
    return res;
}

// Calculates frequency (in Hz) of a note
int frequency(string str)
{
    char note, octave, accidental;
    char alpha[10] = "CDEFGAB";
    //printf("Enter a note such as: A#8\n");
    //scanf("%s", str);///B4
    int i = 0, octave_int, a_pos = 5, str_pos = 0, len = strlen(str), dif, fr_int;
    double fr = 0.0;

    ///Insert into note, accidental and octave
    ///based on string length
    if (len == 2)
    {
        note = str[0];
        octave = str[1];
        accidental = ' ';
    }
    else
    {
        note = str[0];
        accidental = str[1];
        octave = str[2];
    }

    octave_int = octave - '0';

    //printf("Note = %c\nAccidental = %c\nOctave = %d\n", note, accidental, octave_int);

    ///Find the n
    for (i = 0; i < 7; i++)
    {
        if (alpha[i] == note)
        {
            str_pos = i;
            break;
        }
    }

    int n = str_pos - a_pos;
    //printf("n = %d\n", n);

    ///Distance calucation relative to note A

    if (n == 0)
    {
        if (accidental == '#')
            n++;
        else if (accidental == 'b')
            n--;
    }

    else if (n == 1 & accidental == ' ')
        n++;

    else if (n == -1)
    {
        if (accidental == ' ')
            n--;
        else if (accidental == 'b')
            n -= 2;
    }

    else if (n == -2)
    {
        if (accidental == '#')
            n--;
        else if (accidental == ' ')
            n -= 2;
    }

    else if (n == -3)
    {
        if (accidental == ' ')
            n -= 2;
        else if (accidental == 'b')
            n -= 3;
    }

    else if (n == -4)
    {
        if (accidental == '#')
            n -= 2;
        else if (accidental == ' ')
            n -= 3;
        else if (accidental == 'b')
            n -= 4;
    }

    else if (n == -5)
    {
        if (accidental == '#')
            n -= 3;
        else if (accidental == ' ')
            n -= 4;
    }

    ///Distance calc ends here

    //printf("n = %d\n", n);
    int res = calculation(accidental, octave_int, n);

    return res;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, "") == 0)
        return true;
    else
        return false;
}

int calculation(char accidental, int octave_int, int n)
{
    double fr = 0.0;
    int dif, fr_int;

    if (octave_int == 4)
        fr = 440.0;
    else if (octave_int > 4)
    {
        dif = octave_int - 4;
        fr = 440.0 * (2 * dif);
    }
    else if (octave_int < 4)
    {
        dif = 4 - octave_int;
        fr = 440.0 / (2 * dif);
    }


    if (accidental == '#' || n >= 0)
        fr *= pow(2, (n / 12.0));
    else if (accidental == 'b' || n < 0)
        fr /= pow(2, (abs(n) / 12.0));

    fr_int = round(fr);

    return fr_int;
}