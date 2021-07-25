"""
Encryption4 uses several delimeters otherwise same as encryption 3
"""
import random
import string


def createRandList(num_chars, not_allowed):
    """
    :param num_chars: the number of characters to generate values for
    :param not_allowed: list of values that cannot be used, such as the delimiter
    :return: 
    """
    result = []
    # All printable characters can be used
    accepted_chars = list(string.printable)
    # Apart from ' as used for string and others used for newline or weird spaces the space is used as the middle delimiter during decryption
    for banned in ["'", '\t', '\n', '\r', " ", '\x0b', '\x0c']:
        accepted_chars.remove(banned)

    # For each letter
    i = 0
    while i < num_chars:
        key = []
        # Get a random amount of letters from 4 to 9
        for j in range(random.randint(4, 10)):
            # Get a random character
            key.append(random.choice(accepted_chars))

        # All need to be unique
        if key not in result:
            noDivider = True
            #Also need to not have dividers
            for banned in not_allowed:
                if banned in key:
                    noDivider = False
                    #No need to look for other dividers
                    break

            if noDivider:
                result.append("".join(key))
                i += 1

    return result


accepted_chars = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
dividers = ["sk$v", "$$", "#]2f", ";lkjw"]

print("The accepted characters are:", accepted_chars)
rand_list = createRandList(len(accepted_chars), dividers)

key = [
    accepted_chars,
    rand_list
]


while True:
    plainText = input("Please enter text: ")
    choice = input("e or d to encrypt or decrypt (anything else to exit): ")

    if choice == "e":
        encrypted_list = []
        for letter in plainText:
            index = key[0].index(letter)
            encrypted_list.append(key[1][index])
        encrypted_text = encrypted_list[0]
        for i in range(1, len(encrypted_list)):
            encrypted_text += random.choice(dividers) + encrypted_list[i]
        print(encrypted_text)

    elif choice == "d":
        decryptedText = []
        for divider in dividers:
            plainText = plainText.replace(divider, " ")

        words = plainText.split()

        for word in words:
            # Get the index of the word
            try:
                index = key[1].index(word)
                decryptedText.append(key[0][index])

            except:
                print("The value doesn't fit in the dictionary")

        print("".join(decryptedText))

    else:
        break




# Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ