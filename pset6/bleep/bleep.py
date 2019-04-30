from cs50 import get_string
from sys import argv, exit


def main():

    # Check for command line argument
    if (len(argv) != 2):
        print("Usage: python bleep.py dictionary")
        exit(1)

    # Open file & run operation
    try:
        with open(argv[1], "r") as file:

            # Read lines of file
            all_lines = file.readlines()

            # Create a set where each line is an element
            banned_words = set(line.strip() for line in all_lines)

            # Input message
            print("Enter your message")
            message = get_string()

            # Tokenize input string into words
            words = message.split()

            # Convert banned words into asterisks(*)
            for word in words:
                lowercased_word = word.lower()
                if lowercased_word in banned_words:
                    index = words.index(word)
                    words[index] = "*" * len(word)

            # Print the list as a sentence
            for word in words:
                # print the last element of words with \n
                if word == words[-1]:
                    print(word)
                # Print other words with a space following it
                else:
                    print(word, end=" ")

    # If file can't be opened
    except OSError:
        print("Can not open")


if __name__ == "__main__":
    main()