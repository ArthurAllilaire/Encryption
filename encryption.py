import random

from mirror import mirrorStringNtimes, createMirrorList
from enigma import *
from changeChars import encryptStr, decryptStr, createEncryptionKey, createDecryptionKey

#always the same encryption for now
#random.seed(0)

#Global parameters for encryption
numTimesMirror = 10

def encrypt(message, mirrorList, enigma, encryptionKey, dividers):
    """
    Passes the message first through the
    :param message: The message to be encrypted
    :param mirrorList: The list to be passed to mirrorStringNtimes defining how to mirror the string
    :param enigma: The enigma used to encrypt
    :param encryptionKey: The key used to encrypt the message once passed through enigma and mirrored
    :return: The encrypted message
    """
    #Initialise the enigma
    #enigma = Enigma(EnigmaSettings[0], EnigmaSettings[1], EnigmaSettings[2], EnigmaSettings[3])
    # First pass it through the enigma
    enigma_encrypted = enigma.encrypt_message(message)
    #Mirror it
    mirror_encrypted = mirrorStringNtimes(enigma_encrypted, mirrorList)
    substitute_encrypted = encryptStr(mirror_encrypted, dividers, encryptionKey)
    return substitute_encrypted


def decrypt(message, mirrorList, enigma, decryptionKey, dividers):
    """
    Passes the message first through the
    :param message: The message to be decrypted
    :param mirrorList: The list to be passed to mirrorStringNtimes (that was used to mirror the original message) defining how to reverse mirror the string
    :param enigma: The enigma machine used to encrypt it
    :param decryptionKey: The key used to encrypt the message once passed through enigma and mirrored
    :return: The encrypted message
    """
    un_substituted = decryptStr(message, dividers, decryptionKey)
    un_mirror = mirrorStringNtimes(un_substituted, mirrorList, True)
    decrypted = enigma.decrypt_message(un_mirror)
    return decrypted

mes_to_encrypt = "Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz This is a cool message isn't it??????"


mirror_list = createMirrorList(10, len(mes_to_encrypt)//3)

AcceptedChars= list(string.printable)[:-5]
#Stacker, reflector, accepted chars,
Stacker = createStacker(AcceptedChars, len(AcceptedChars)//3)
#Stacker with all the wires attached
Reflector = createReflector(AcceptedChars, len(AcceptedChars))
RotorSettings = [10, 35, 77, 19, 0]

enigma = Enigma(Stacker, Reflector, AcceptedChars, RotorSettings)


#DECRYPTION SETTINGS
#CHANGECHARS VALS

dividers = ["sk$v", "#2$", "#]2f", ";lkjw", "&)"]

encryption_key = createEncryptionKey(AcceptedChars, dividers)
decryption_key = createDecryptionKey(encryption_key)


encrypted_mes = encrypt(mes_to_encrypt, mirror_list, enigma, encryption_key, dividers)
decrypted_mes = decrypt(encrypted_mes, mirror_list, enigma, decryption_key, dividers)

print(mes_to_encrypt)
print("Encrypted Message:", encrypted_mes)
print(decrypted_mes)






# while True:
#     plainText = input("Please enter text: ")
#     choice = input("e or d to encrypt or decrypt (anything else to exit): ")
#
#     #specifies ub but uses default lb
#     mirrorList = createMirrorList(numTimesMirror, len(plainText)//3)
#
#     print(mirrorList)
#
#     if choice == "e":
#         output = encrypt(mirrorList)
#
#     elif choice == "d":
#         toChange = input(f"The current mirror list is: {mirrorList}. Would you like to change it (yes/no)? ")
#         if toChange == "yes":
#             mirrorList = list(input(f"Input new mirror list: "))
#         output = decrypt(mirrorList)
#
#
#     else:
#         break
#
#     print(output)




