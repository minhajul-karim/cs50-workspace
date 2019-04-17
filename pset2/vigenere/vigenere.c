#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//function prototypes

int base_pos(int arr[], char c);

int encipher_calculation(int base, int k);

void encipher(string original_text, int cap_arr[], int sm_arr[], int len, int key_int[], int key_len);

void create_alphabetical_indices(int cap_arr[], int sm_arr[]);

void string_to_int(char key[], int key_int[], int capital_array[], int small_array[]);

int main(int argc, string argv[])
{
    string plain_text;
    int capital_array[26], small_array[26], key_int[100];
    int i, j, length;
    char key[100];

    //creating alphabetic indices of capital and small letters
    create_alphabetical_indices(capital_array, small_array);

    //Check the argument count
    if (argc != 2)
    {
        printf("Error\n");
        return 1;
    }
    else
    {
        // copyting argv[1] to string key
        strcpy(key, argv[1]);

        //The length of key
        int key_len = strlen(key);

        //checking if key has any non-alphabetical character
        for (i = 0; i < key_len; i++)
        {
            if (!isalpha(key[i]))
            {
                printf("Error\n");
                return 1;
            }
        }

        //turning key into alphabetical indices
        string_to_int(key, key_int, capital_array, small_array);

        //print key_int
        /*for (i = 0; i < key_len; i++)
        {
            printf("%d ", key_int[i]);
        }
        printf("\n");*/

        //prompting for plaintext
        plain_text = get_string("plaintext: ");

        //Calculate the length of plaintext
        length = strlen(plain_text);

        //Encipher
        encipher(plain_text, capital_array, small_array, length, key_int, key_len);

    }
    return 0;
}

//Calculates the index of a letter in alphabetical indices
int base_pos(int arr[], char c)
{
    int i, base_position = 0;
    for (i = 0; i < 26; i++)
    {
        if (arr[i] == c)
        {
            base_position = i;
            break;
        }
    }
    return base_position;
}



//calculates the the index of encrypted letter
int encipher_calculation(int base, int k)
{
    int index = (base + k) % 26;
    return index;
}


//Checks each letter of plaintext and prints with encryption if applicable
void encipher(string original_text, int cap_arr[], int sm_arr[], int len, int key_int[], int key_len)
{
    int i, j = 0, x, encrypted_index = 0;
    printf("ciphertext: ");
    for (i = 0; i < len; i++)
    {
        if (isalpha(original_text[i]))
        {
            if (isupper(original_text[i]))
            {
                int base = base_pos(cap_arr, original_text[i]);
                x = j % key_len;
                encrypted_index = encipher_calculation(base, key_int[x]);
                printf("%c", cap_arr[encrypted_index]);
            }
            else
            {
                int base = base_pos(sm_arr, original_text[i]);
                x = j % key_len;
                encrypted_index = encipher_calculation(base, key_int[x]);
                printf("%c", sm_arr[encrypted_index]);
            }
            j++;
        }
        else
        {
            printf("%c", original_text[i]);
        }
    }
    printf("\n");
}


//Creates alphabetical indices for both capital and small letters
void create_alphabetical_indices(int cap_arr[], int sm_arr[])
{
    int i, letter_cap = 65, letter_sm = 97;

    //filling sm_arr with cap letters
    for (i = 0; ; i++)
    {
        if (letter_cap > 90)
        {
            break;
        }
        else
        {
            cap_arr[i] = letter_cap;
            letter_cap++;
        }
    }

    //filling sm_arr with small letters

    for (i = 0; ; i++)
    {
        if (letter_sm > 122)
        {
            break;
        }
        else
        {
            sm_arr[i] = letter_sm;
            letter_sm++;
        }
    }
}

void string_to_int(char key[], int key_int[], int capital_array[], int small_array[])
{
    int i, j;
    for (i = 0; key[i] != '\0'; i++)
    {
        if (isupper(key[i]))
        {
            for (j = 0; j < 26; j++)
            {
                if (key[i] == capital_array[j])
                {
                    key_int[i] = j;
                }
            }
        }
        else
        {
            for (j = 0; j < 26; j++)
            {
                if (key[i] == small_array[j])
                {
                    key_int[i] = j;
                }
            }
        }
    }
}