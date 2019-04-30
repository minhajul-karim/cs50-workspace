import sys


# Check the argument count
if (len(sys.argv) != 2):
    print("Usage: ./vigenere keyword")
    sys.exit(1)
    
# Check if key i.e. argv[1] has any non-alphabetical character
if not (sys.argv[1].isalpha()):
    print("Usage: ./vigenere keyword")
    sys.exit(1)
    
# Take input
plaintext = input("plaintext: ")
key = sys.argv[1]

# Variables
counter = -1
len_of_plaintext = len(plaintext)
len_of_key = len(key)

print("ciphertext: ", end="")

# Iterate through all chars of plaintext
for i in range(len_of_plaintext):

    # if i'th letter of plaintext is a letter
    if (plaintext[i].isalpha()):
        counter = counter + 1
        
        # if i'th letter of plaintext is lowercase
        if plaintext[i].islower():
            current_plaintext_pos = ord(plaintext[i]) - 97
            current_key_index = counter % len_of_key
            
            # Check the case the current index of key
            if key[current_key_index].islower():
                shift = ord(key[current_key_index]) - 97
            else:
                shift = ord(key[current_key_index]) - 65
                
            # Index of encrypted char for plaintext[i]
            ci = (current_plaintext_pos + shift) % 26
            
            # Encrypted char
            new_char = ci + 97
            
            # Print the equivalent char resided in new_char
            print(chr(new_char), end="")
        
        # if i'th letter of plaintext is uppercase
        else:
            current_plaintext_pos = ord(plaintext[i]) - 65
            current_key_index = counter % len_of_key
            
            # Check the case the current index of key
            if key[current_key_index].islower():
                shift = ord(key[current_key_index]) - 97
            else:
                shift = ord(key[current_key_index]) - 65
                
            # Index of encrypted char for plaintext[i]
            ci = (current_plaintext_pos + shift) % 26
            
            # Encrypted char
            new_char = ci + 65
            
            # Print the equivalent char resided in new_char
            print(chr(new_char), end="")
     
    else:
        print(plaintext[i], end="")
        
print()
