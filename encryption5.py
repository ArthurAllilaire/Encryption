"""
Encryption 5 is the same as encryption 4 but uses a dictionary instead of a list
"""
import random
import string

def notIn(val, listDict):
    """
    checks if key is in any of the
    :param key:
    :param listDict: keys are letters values are lists of strings
    :return: Boolean true if key is already in twodarray, even if only a substring
    """
    for keyInner in listDict:
        for keyVal in listDict[keyInner]:
            if val in keyVal:
                return False

    return True

def noDivider(dividers, strVal):
    """
    :param dividers: List of dividers that cannot be present in the strings
    :param strVal: The string that could contain the dividers
    :return: boolean, False if dividers are present otherwise True
    """
    for divider in dividers:
        if divider in strVal:
            return False
        else:
            # Need to check that if the divider is added to the str at the end
            # The divider doesn't appear earlier
            temp = strVal + divider
            # Get the index of where the divider appears
            index = temp.find(divider)
            # If it is any earlier than the len(string) then return false
            if index < len(strVal):
                return False

    return True


def createEncryptionKey(chars, not_allowed):
    """
    :param chars: the characters to generate values for
    :param not_allowed: list of values that cannot be used, such as the delimiter
    :return: A dictionary
    """
    result = {}
    # All printable characters can be used
    accepted_chars = list(string.printable)
    # Apart from ' as used for string and others used for newline or weird spaces the space is used as the middle delimiter during decryption
    for banned in ["'", '\t', '\n', '\r', " ", '\x0b', '\x0c']:
        accepted_chars.remove(banned)

    for char in chars:
        valList = []
        # Have 4 options for every value
        for i in range(4):
            val = []
            # Get a random amount of letters from 4 to 9
            for j in range(random.randint(4, 10)):
                # Get a random character
                val.append(random.choice(accepted_chars))

            #Make list into string
            val = "".join(val)
            # Before adding to the valList make sure it is unique and doesn't have dividers
            if notIn(val,result) and noDivider(not_allowed, val):
                valList.append(val)
        result[char] = valList

    return result

def createDecryptionKey(encryptionKey):
    """
    It reverses the encryption key
    :param encryptionKey:
    :return:
    """
    decryptionKey = {}
    for originalLetter, valueList in encryptionKey.items():
        for value in valueList:
            decryptionKey[value] = originalLetter

    return decryptionKey

def encrypt():
    """
    :return:
    """
    encrypted_list = []
    for letter in plainText:
        # Take one random value from the list associated with the value key
        encrypted_list.append(random.choice(encryptionKey[letter]))

    encrypted_text = encrypted_list[0]
    for i in range(1, len(encrypted_list)):
        encrypted_text += random.choice(dividers) + encrypted_list[i]

    return encrypted_text

def decrypt():

    global plainText
    decryptedText = []

    for divider in dividers:
        plainText = plainText.replace(divider, " ")

    words = plainText.split()

    for word in words:
        decryptedText += decryptionKey.get(word, "")

    return "".join(decryptedText)

accepted_chars = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
dividers = ["sk$v", "$$", "#]2f", ";lkjw"]

print("The accepted characters are: ", accepted_chars)
encryptionKey = createEncryptionKey(accepted_chars, dividers)
decryptionKey = createDecryptionKey(encryptionKey)


while True:
    plainText = input("Please enter text: ")
    choice = input("e or d to encrypt or decrypt (anything else to exit): ")

    if choice == "e":
        output = encrypt()

    elif choice == "d":
        output = decrypt()


    else:
        break

    print(output)



# Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz