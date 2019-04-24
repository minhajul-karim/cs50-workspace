/**** The basic idea is adopted from
https://www.geeksforgeeks.org/print-all-combinations-of-given-length/ ****/

#include <iostream>
#include <string>
#include <crypt.h>
#include <cstring>

using namespace std;

void crack(char alpha[], string prefix, char arg[], char salt[], int n, int k);

int main(int argc, char** argv)
{
    // Check for appropriate user input
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./crack <hashed_key>\n");
        return 0;
    }

    // Separate the salt form argv[1]
    char salt[3];
    strncpy(salt, argv[1], 2);
    salt[2] = '\0';

    // String of alphabets
    char letters[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Number of characters in letters[]
    int elements = 52;

    // Max length of a password
    int max_password_len = 5;

    // Check for password of length 1 to 5(max)
    for (int pwd_len = 1; pwd_len <= max_password_len; pwd_len++)
    {
        crack(letters, "", argv[1], salt, elements, pwd_len);
    }

    printf("not found\n");

    return 0;
}

void crack(char alpha[], string prefix, char arg[], char salt[], int n, int k)
{
    if (k == 0)
    {
        // Convert string into const char*
        const char* c = prefix.c_str();

        // Check if the encryption of current prefix matches user input i.e. argv[1]
        if (strcmp(arg, crypt(c, salt)) == 0)
        {
            // Print the current prefix and exit
            cout << prefix << endl;
            exit(0);
        }

        return;
    }

    for (int i = 0; i < n; i++)
    {
        // Add a character to the prefix
        string newPrefix = prefix + alpha[i];
        crack(alpha, newPrefix, arg, salt, n, k - 1);
    }
}
