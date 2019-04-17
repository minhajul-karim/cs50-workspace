#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct _trie
{
    struct _trie* alphabet[27];
    bool isWord;
}
trie;

/// Global trie
trie* root_node = NULL;

/// Protos
void allocate_root();
trie* create();
bool load(const char *dictionary);
bool check(const char *word);
void delete_root(trie* root_node);
bool unload(void);

int main()
{
    char *file = "dic.txt";

    bool res = load(file);
    printf("load status = %d\n", res);

    char *str = "a";
    printf("%s\n", str);
    res = check(str);
    printf("check status = %d\n", res);
    //delete_root(root_node);
    res = unload();
    printf("unload status = %d\n", res);

    return 0;
}

// Create root
trie* create()
{
    /// Create a new trie
    trie* new_trie = (trie*)malloc(sizeof(trie));

    /// Check if memory has been allocated
    if (new_trie == NULL)
    {
        fprintf(stderr, "Can not allocate memory\n");
        exit(1);
    }

    new_trie->isWord = false;

    /// Setting all trie pointers to NULL
    for (int i = 0; i < 27; i++)
        new_trie->alphabet[i] = NULL;

    return new_trie;
}

bool load(const char *dictionary)
{
    FILE* fp = fopen(dictionary, "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Error reading\n");
        exit(1);
    }

    int count = 0;
    char string[100];
    //allocate_root();
    root_node = create();

    /// Iterate through the file by scanning each word
    while(fscanf(fp, "%s", string) != EOF)
    {
        printf("Inserting %s.. which's len is = ", string);
        /// Loading process initiates here

        int i, index, len = strlen(string);
        printf("%d\n", len);
        trie* trav = root_node;

        /// Loop through the string
        for (i = 0; i < len; i++)
        {
            printf("i = %d :: ", i);
            /// Check if the word contains only alphabets & '
            if (string[i] >= 'a' && string[i] <= 'z')
            {
                index = string[i] - 97;
                printf("index for %c is %d\n", string[i], index);
            }

            else if (string[i] == '\'')
            {
                index = 26;
                printf("index for %c is %d\n", string[i], index);
            }

            /// If node string[index] is not created
            if (trav->alphabet[index] == NULL)
            {
                printf("trav->alphabet[%d] is null. Creating a child...\n", index);
                trav->alphabet[index] = create();
            }

            if (i == len - 1 && !(trav->isWord))
            {
                printf("This is the last letter of %s. Curr stts of trav->isWord is %d\n", string, trav->isWord);
                trav->isWord = true;
                printf("Set trav->isWord = true; Loading done. Present stts of trav->isWord = %d.\n", trav->isWord);
                //return true;
                count++;
            }

            printf("trav = trav->alphabet[%d]\n", index);
            trav = trav->alphabet[index];
        }

        // Loading process ends here
    }

    fclose(fp);

    if (count > 0)
        return true;
    else
        return false;
}

void delete_root(trie* root)
{
    printf("DEBUG: Received root. Searching if root->alphabet[i] != NULL\n");
    for (int i = 0; i < 27; i++)
    {
        if (root->alphabet[i] != NULL)
        {
            printf("DEBUG: Found NUll at i = %d. Recursing by unload(root->alphabet[%d])\n", i, i);
            delete_root(root->alphabet[i]);
            printf("DEBUG: Returned from unload(). Curr pos of i = %d\n", i);
        }
    }

    printf("DEBUG: Free root. Return\n");
    free(root);
    root = NULL;
    return;
}

bool unload(void)
{
    if (root_node != NULL)
    {
        delete_root(root_node);
        return true;
    }
    else
        return false;
}

bool check(const char *word)
{
    printf("Checking for %s which's len is ", word);
    int i, index, len = strlen(word);
    printf("%d\n", len);
    trie* trav = root_node;

    /// Loop through the word
    for (i = 0; i < len; i++)
    {
        printf("i = %d :: ", i);
        /// Check if the word contains only alphabets & '
        if (word[i] >= 'a' && word[i] <= 'z')
        {
            index = word[i] - 97;
            printf("index for %c is %d\n", word[i], index);
        }
        else if (word[i] >= 'A' && word[i] <= 'Z')
        {
            index = word[i] - 65;
            printf("index for %c is %d\n", word[i], index);
        }
        else if (word[i] == '\'')
        {
            index = 26;
            printf("index for %c is %d\n", word[i], index);
        }

        /// If node word[index] is not created
        if (trav->alphabet[index] == NULL)
        {
            printf("trav->alphabet[index] is NULL. Doesn't exits. Returning false\n");
            // The word does not exist
            return false;
        }

        if ((i == len - 1) && (trav->isWord))
        {
            printf("This is the last letter of %s. Curr stts of trav->isWord is %d. ", word, trav->isWord);
            printf("Returning true. Exist\n");
            // The word exists
            return true;
        }

        // Make the child node a parent node
        printf("trav = trav->alphabet[%d]\n", index);
        trav = trav->alphabet[index];

    }

    printf("Returning false :(\n");
    return false;
}