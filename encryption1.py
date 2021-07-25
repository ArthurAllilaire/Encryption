
while True:
    plainText = input("Please enter text: ")
    choice = input("e or d to encrypt or decrypt (anything else to exit): ")

        
    if choice == 'e': 
        encryptedText = ''
        for letter in plainText:
            if letter == ' ':
                encryptedText += 'I'
            elif letter == 'a':
                encryptedText += 'y'
            elif letter == 'b':
                encryptedText += 'X'
            elif letter == 'c':
                encryptedText += 'm'
            elif letter == 'd':
                encryptedText += 's'
            elif letter == 'e':
                encryptedText += 'q'
            elif letter == 'f':
                encryptedText += 'w'
            elif letter == 'g':
                encryptedText += 'V'
            elif letter == 'h':
                encryptedText += 'i'
            elif letter == 'i':
                encryptedText += 'o'
            elif letter == 'j':
                encryptedText += 'K'
            elif letter == 'k':
                encryptedText += 'S'
            elif letter == 'l':
                encryptedText += 'r'
            elif letter == 'm':
                encryptedText += 'D'
            elif letter == 'n':
                encryptedText += 'L'
            elif letter == 'o':
                encryptedText += 'O'
            elif letter == 'p':
                encryptedText += 'P'
            elif letter == 'q':
                encryptedText += 'u'
            elif letter == 'r':
                encryptedText += 'b'
            elif letter == 's':
                encryptedText += 'x'
            elif letter == 't':
                encryptedText += 'C'
            elif letter == 'u':
                encryptedText += 'W'
            elif letter == 'v':
                encryptedText += 'l'
            elif letter == 'w':
                encryptedText += 'k'
            elif letter == 'x':
                encryptedText += 'z'
            elif letter == 'y':
                encryptedText += 'N'
            elif letter == 'z':
                encryptedText += 'F'
            elif letter == 'A':
                encryptedText += 'E'
            elif letter == 'B':
                encryptedText += 'J'
            elif letter == 'C':
                encryptedText += 'Z'
            elif letter == 'D':
                encryptedText += 'U'
            elif letter == 'E':
                encryptedText += 'R'
            elif letter == 'F':
                encryptedText += 'g'
            elif letter == 'G':
                encryptedText += ' '
            elif letter == 'H':
                encryptedText += 'B'
            elif letter == 'I':
                encryptedText += 'T'
            elif letter == 'J':
                encryptedText += 'Y'
            elif letter == 'K':
                encryptedText += 'n'
            elif letter == 'L':
                encryptedText += 'a'
            elif letter == 'M':
                encryptedText += 'h'
            elif letter == 'N':
                encryptedText += 'A'
            elif letter == 'O':
                encryptedText += 'M'
            elif letter == 'P':
                encryptedText += 'f'
            elif letter == 'Q':
                encryptedText += 'H'
            elif letter == 'R':
                encryptedText += 'c'
            elif letter == 'S':
                encryptedText += 'd'
            elif letter == 'T':
                encryptedText += 'Q'
            elif letter == 'U':
                encryptedText += 'v'
            elif letter == 'V':
                encryptedText += 'e'
            elif letter == 'W':
                encryptedText += 'p'
            elif letter == 'X':
                encryptedText += 'G'
            elif letter == 'Y':
                encryptedText += 'j'
            elif letter == 'Z':
                encryptedText += 't'

        print(encryptedText)
    
    elif choice == 'd': 
        decryptedText = ''
        for letter in plainText:
            if letter == 'I':
                decryptedText += ' '
            elif letter == 'y':
                decryptedText += 'a'
            elif letter == 'X':
                decryptedText += 'b'
            elif letter == 'm':
                decryptedText += 'c'
            elif letter == 's':
                decryptedText += 'd'
            elif letter == 'q':
                decryptedText += 'e'
            elif letter == 'w':
                decryptedText += 'f'
            elif letter == 'V':
                decryptedText += 'g'
            elif letter == 'i':
                decryptedText += 'h'
            elif letter == 'o':
                decryptedText += 'i'
            elif letter == 'K':
                decryptedText += 'j'
            elif letter == 'S':
                decryptedText += 'k'
            elif letter == 'r':
                decryptedText += 'l'
            elif letter == 'D':
                decryptedText += 'm'
            elif letter == 'L':
                decryptedText += 'n'
            elif letter == 'O':
                decryptedText += 'o'
            elif letter == 'P':
                decryptedText += 'p'
            elif letter == 'u':
                decryptedText += 'q'
            elif letter == 'b':
                decryptedText += 'r'
            elif letter == 'x':
                decryptedText += 's'
            elif letter == 'C':
                decryptedText += 't'
            elif letter == 'W':
                decryptedText += 'u'
            elif letter == 'l':
                decryptedText += 'v'
            elif letter == 'k':
                decryptedText += 'w'
            elif letter == 'z':
                decryptedText += 'x'
            elif letter == 'N':
                decryptedText += 'y'
            elif letter == 'F':
                decryptedText += 'z'
            elif letter == 'E':
                decryptedText += 'A'
            elif letter == 'J':
                decryptedText += 'B'
            elif letter == 'Z':
                decryptedText += 'C'
            elif letter == 'U':
                decryptedText += 'D'
            elif letter == 'R':
                decryptedText += 'E'
            elif letter == 'g':
                decryptedText += 'F'
            elif letter == ' ':
                decryptedText += 'G'
            elif letter == 'B':
                decryptedText += 'H'
            elif letter == 'T':
                decryptedText += 'I'
            elif letter == 'Y':
                decryptedText += 'J'
            elif letter == 'n':
                decryptedText += 'K'
            elif letter == 'a':
                decryptedText += 'L'
            elif letter == 'h':
                decryptedText += 'M'
            elif letter == 'A':
                decryptedText += 'N'
            elif letter == 'M':
                decryptedText += 'O'
            elif letter == 'f':
                decryptedText += 'P'
            elif letter == 'H':
                decryptedText += 'Q'
            elif letter == 'c':
                decryptedText += 'R'
            elif letter == 'd':
                decryptedText += 'S'
            elif letter == 'Q':
                decryptedText += 'T'
            elif letter == 'v':
                decryptedText += 'U'
            elif letter == 'e':
                decryptedText += 'V'
            elif letter == 'p':
                decryptedText += 'W'
            elif letter == 'G':
                decryptedText += 'X'
            elif letter == 'j':
                decryptedText += 'Y'
            elif letter == 't':
                decryptedText += 'Z'

        print(decryptedText)
        
    else:
        break