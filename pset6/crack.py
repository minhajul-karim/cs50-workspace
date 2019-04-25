import sys
import crypt

def main():
    # Check for appropriate input
    if (len(sys.argv) != 2):
        print("Error")
        exit(1)

    # Retrive the salt form argv[1]
    salt = sys.argv[1][:2]

    # String of alphabets
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Number of characters in letters[]
    elements = len(letters);

    # Max length of a password
    max_password_len = 5;

    for pwd_len in range(1, max_password_len + 1):
        crack(letters, "", sys.argv[1], salt, elements, pwd_len)

    print("NOT FOUND")


# Crack function
def crack(alpha, prefix, arg, salt, n, k):
    if k == 0:
        # Check if the ecryption of current prefix & salt mathches argv[1]
        if crypt.crypt(prefix, salt) == arg:
            print(prefix)
            exit(0)

        return

    # Create every possible combination of alphabets of given length i.e. k
    for i in range(n):
        newPrefix = prefix + alpha[i]
        crack(alpha, newPrefix, arg, salt, n, k - 1)

# Run the main function
if __name__ == "__main__":
    main()
