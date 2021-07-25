"""
Encryption 2 is replacement with characters of regular lenth e.g. 5 lettter for a
Can use lists
"""
import random
import string
def createRandList(num_chars, not_allowed):
    """
    :param num_chars: the number of characters to generate values for
    :param not_allowed: list of values that cannot be used
    :return: 
    """
    result = []
    #All printable characters can be used
    accepted_chars = list(string.printable)
    #Apart from ' as used for string and other used for newline
    not_allowed.extend(["'", '\t', '\n', '\r'])
    for banned in not_allowed:
        accepted_chars.remove(banned)
        
    #For each letter
    i = 0
    while i < num_chars:
        key = []
        #Get a random amount of letters from 4 to 9
        for j in range(random.randint(4,10)):
            #Get a random character
            key.append(random.choice(accepted_chars))

        #All need to be unique
        if key not in result:
            result.append("".join(key))
            i += 1
        
    return result

accepted_chars = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)

print("The accepted characters are:", accepted_chars)
rand_list = createRandList(len(accepted_chars), ["*"])

key = [
    accepted_chars,
    rand_list
]

divider = "d"
while True:
    plainText = input("Please enter text: ")
    choice = input("e or d to encrypt or decrypt (anything else to exit): ")

    if choice == "e":
        encrypted_text = []
        for letter in plainText:
            index = key[0].index(letter)
            encrypted_text.append(key[1][index])

        print(divider.join(encrypted_text))

    elif choice == "d":
        decryptedText = []
        words = plainText.split(divider)

        for word in words:
            #Get the index of the word
            try:
                index = key[1].index(word)
                decryptedText.append(key[0][index])

            except:
                print("There was a problem")

        print("".join(decryptedText))

    else:
        break

#Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz