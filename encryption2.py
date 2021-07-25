
while True:
    plainText = input("Please enter text (letters or space): ")
    choice = input("e or d to encrypt or decrypt (anything else to exit): ")

    if choice == 'e': 
        encryptedText = ''
        for letter in plainText:
            if letter == ' ':
                encryptedText += '=]^c'
            elif letter == 'a':
                encryptedText += 'uLwO'
            elif letter == 'b':
                encryptedText += '-d2K'
            elif letter == 'c':
                encryptedText += '5]v:'
            elif letter == 'd':
                encryptedText += 'fOd6'
            elif letter == 'e':
                encryptedText += 'q|Dz'
            elif letter == 'f':
                encryptedText += 'ElIE'
            elif letter == 'g':
                encryptedText += 'uc&g'
            elif letter == 'h':
                encryptedText += '?%#.'
            elif letter == 'i':
                encryptedText += '69Yi'
            elif letter == 'j':
                encryptedText += '^607'
            elif letter == 'k':
                encryptedText += 'PACl'
            elif letter == 'l':
                encryptedText += 'qHc9'
            elif letter == 'm':
                encryptedText += 'jf2,'
            elif letter == 'n':
                encryptedText += '!I0]'
            elif letter == 'o':
                encryptedText += '4YiH'
            elif letter == 'p':
                encryptedText += '@-$a'
            elif letter == 'q':
                encryptedText += 'VT-o'
            elif letter == 'r':
                encryptedText += 'Ac/e'
            elif letter == 's':
                encryptedText += 'Bw}G'
            elif letter == 't':
                encryptedText += 'ZOn&'
            elif letter == 'u':
                encryptedText += 'm"<P'
            elif letter == 'v':
                encryptedText += '&gE}'
            elif letter == 'w':
                encryptedText += 'Tuk1'
            elif letter == 'x':
                encryptedText += 'G$Qg'
            elif letter == 'y':
                encryptedText += 'oPcm'
            elif letter == 'z':
                encryptedText += 'sl-R'
            elif letter == 'A':
                encryptedText += 'OVS#'
            elif letter == 'B':
                encryptedText += 'Y=]~'
            elif letter == 'C':
                encryptedText += '.}KM'
            elif letter == 'D':
                encryptedText += 'Z]Z?'
            elif letter == 'E':
                encryptedText += 'E?iu'
            elif letter == 'F':
                encryptedText += ']r;X'
            elif letter == 'G':
                encryptedText += 'ox98'
            elif letter == 'H':
                encryptedText += ':c^I'
            elif letter == 'I':
                encryptedText += ':&nz'
            elif letter == 'J':
                encryptedText += '+8`<'
            elif letter == 'K':
                encryptedText += '.E|1'
            elif letter == 'L':
                encryptedText += '&uL?'
            elif letter == 'M':
                encryptedText += '?r#]'
            elif letter == 'N':
                encryptedText += 'B;HS'
            elif letter == 'O':
                encryptedText += '"^5*'
            elif letter == 'P':
                encryptedText += '._oe'
            elif letter == 'Q':
                encryptedText += 'D2/7'
            elif letter == 'R':
                encryptedText += 'Q)[|'
            elif letter == 'S':
                encryptedText += '%jy7'
            elif letter == 'T':
                encryptedText += 'A6r;'
            elif letter == 'U':
                encryptedText += '24R:'
            elif letter == 'V':
                encryptedText += 'KJ80'
            elif letter == 'W':
                encryptedText += 'gk7+'
            elif letter == 'X':
                encryptedText += 'FQd_'
            elif letter == 'Y':
                encryptedText += 'HQpE'
            elif letter == 'Z':
                encryptedText += 'B3T{'

        print(encryptedText)
    
    elif choice == 'd': 
        decryptedText = ''
        last_index = 0
        for index in range(0, len(plainText), 4):
            word = plainText[last_index:index]
            print(word)
            if word == '=]^c':
                decryptedText += ' '
            elif word == 'uLwO':
                decryptedText += 'a'
            elif word == '-d2K':
                decryptedText += 'b'
            elif word == '5]v:':
                decryptedText += 'c'
            elif word == 'fOd6':
                decryptedText += 'd'
            elif word == 'q|Dz':
                decryptedText += 'e'
            elif word == 'ElIE':
                decryptedText += 'f'
            elif word == 'uc&g':
                decryptedText += 'g'
            elif word == '?%#.':
                decryptedText += 'h'
            elif word == '69Yi':
                decryptedText += 'i'
            elif word == '^607':
                decryptedText += 'j'
            elif word == 'PACl':
                decryptedText += 'k'
            elif word == 'qHc9':
                decryptedText += 'l'
            elif word == 'jf2,':
                decryptedText += 'm'
            elif word == '!I0]':
                decryptedText += 'n'
            elif word == '4YiH':
                decryptedText += 'o'
            elif word == '@-$a':
                decryptedText += 'p'
            elif word == 'VT-o':
                decryptedText += 'q'
            elif word == 'Ac/e':
                decryptedText += 'r'
            elif word == 'Bw}G':
                decryptedText += 's'
            elif word == 'ZOn&':
                decryptedText += 't'
            elif word == 'm"<P':
                decryptedText += 'u'
            elif word == '&gE}':
                decryptedText += 'v'
            elif word == 'Tuk1':
                decryptedText += 'w'
            elif word == 'G$Qg':
                decryptedText += 'x'
            elif word == 'oPcm':
                decryptedText += 'y'
            elif word == 'sl-R':
                decryptedText += 'z'
            elif word == 'OVS#':
                decryptedText += 'A'
            elif word == 'Y=]~':
                decryptedText += 'B'
            elif word == '.}KM':
                decryptedText += 'C'
            elif word == 'Z]Z?':
                decryptedText += 'D'
            elif word == 'E?iu':
                decryptedText += 'E'
            elif word == ']r;X':
                decryptedText += 'F'
            elif word == 'ox98':
                decryptedText += 'G'
            elif word == ':c^I':
                decryptedText += 'H'
            elif word == ':&nz':
                decryptedText += 'I'
            elif word == '+8`<':
                decryptedText += 'J'
            elif word == '.E|1':
                decryptedText += 'K'
            elif word == '&uL?':
                decryptedText += 'L'
            elif word == '?r#]':
                decryptedText += 'M'
            elif word == 'B;HS':
                decryptedText += 'N'
            elif word == '"^5*':
                decryptedText += 'O'
            elif word == '._oe':
                decryptedText += 'P'
            elif word == 'D2/7':
                decryptedText += 'Q'
            elif word == 'Q)[|':
                decryptedText += 'R'
            elif word == '%jy7':
                decryptedText += 'S'
            elif word == 'A6r;':
                decryptedText += 'T'
            elif word == '24R:':
                decryptedText += 'U'
            elif word == 'KJ80':
                decryptedText += 'V'
            elif word == 'gk7+':
                decryptedText += 'W'
            elif word == 'FQd_':
                decryptedText += 'X'
            elif word == 'HQpE':
                decryptedText += 'Y'
            elif word == 'B3T{':
                decryptedText += 'Z'

            #Increment the window
            last_index = index

        print(decryptedText)
        
    else:
        break