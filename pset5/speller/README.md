# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

= According to Merriam-Webster's Medical Dictionary, pneumonoultramicroscopicsilicovolcanoconiosis is a
pneumoconiosis caused by inhalation of very fine silicate or quartz dust.


## According to its man page, what does `getrusage` do?

= It returns resource usage measures.

## Per that same man page, how many members are in a variable of type `struct rusage`?

= 16.

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`,
## even though we're not changing their contents?

= If we pass arguments by value, it creates copies of the variables using the parameters. A variable of type `rusage` consumes
144 bytes of memory. The variables `before` and `after` takes 288 bytes in memory together. It will take another 288 bytes
(total 576 bytes) if we pass the arguments by value. In order to save this amount of memory, we pass by reference here.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file.
## In other words, convince us that you indeed understand how that function's `for` loop works.

= Using the for loop we scan every single character of a given file until we reach EOF using int c = getchar(file_name). We have
declared an string called word[] which will be storing the word that we want to check. We will also be counting the indices of the
string word[], the number of misspelled words, and the total number of words present in that file.

If the character c is an alphabet or an apostrophe, we insert it in the array, increment index by 1. We will continue insertion
until we find any newline character(e.g., ‘\n’), the length of a word does not exceed the maximum word length(e.g., 45), or
the word contains any digit. If any of the above-mentioned situations arises except the first one, we ignore the whole word
we have been inserting.

We will insert a new line character(e.g., ‘\n’) after reaching the same in the input file followed by one or multiple characters.
As we have found a whole word at this point, we will check it’s spelling using a function called check(), calculate the time it
took, and store it’s return value in a variable(e.g., misspelled). If the the word is misspelled, we will increment the number of
misspelled words, print it and fasten our seat-belts as we have to start collecting the next word to check.



## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format
## string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

= `fscanf` terminates the scanning process right away when it reaches space character which will not be helpful to us as
we are going to read files containing words after word separated by spaces.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

= So that the reference which will be passed to the parameters can not be modified.
