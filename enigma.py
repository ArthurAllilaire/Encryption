import string
import random

# random.seed(0)
"""
This is enigma 2.0 a letter can be encrypted to itself and there is a much larger range of possible letters to be passed in and encrypted to, this exponentially increases the number of potential settings.
Num of possible settings = infinity.
Rotors: Can have as many as you want, they each have len(AcceptedChars) possible values
Stacker: Any letter can be mapped to any other letter and to nothing
Reflector: 
If you guess all those settings you deserve to know the encrypted key.
"""
#Global variables
#Every char needs to be used in both encryption and decryption so no whitespace apart from spaces.
AcceptedChars= list(string.printable)[:-5]

def createStacker(AcceptedChars, num_chars):
    """
    Gets num char * 2 values paired together
    :param acceptedChars: The chars to be used
    :param num_chars: The amount of acceptedChars to be mapped to another Char shouldn't be bigger than half of the len(acceptedChars)
    :return: A dictionary mapping num_chars of the acceptedChars
    to another random value from accepted chars
    """
    result = {}
    # Chars taken for key value
    charsToChoose = AcceptedChars.copy()

    for i in range(num_chars):
        # Get a random element from charsToChoose and remove it from the list
        # Rand int includes endpoints so -1 to stay in list range
        key = charsToChoose.pop(random.randint(0, len(charsToChoose) - 1))
        result[key] = charsToChoose.pop(random.randint(0, len(charsToChoose) - 1))

    return result

def createReflector(acceptedChars, num_chars):
    """

    :param acceptedChars: The chars to be used
    :param num_chars: The amount of acceptedChars to be mapped to another Char
    :return: A dictionary mapping num_chars of the acceptedChars
    to another random value from accepted chars
    """
    result = {}
    # Chars taken for key value
    charsToChoose = acceptedChars.copy()
    # Chars taken for value value the encrypted letter
    charsToSet = acceptedChars.copy()

    for i in range(num_chars):
        # Get a random element from charsToChoose and remove it from the list
        # Rand int includes endpoints so -1 to stay in list range
        key = charsToChoose.pop(random.randint(0, len(charsToChoose) - 1))
        value = charsToSet.pop(random.randint(0, len(charsToSet) - 1))
        # A key could map to the same value
        result[key] = value

    return result


Stacker = createStacker(AcceptedChars, len(AcceptedChars)//3)
#Stacker with all the wires attached
Reflector = createReflector(AcceptedChars, len(AcceptedChars))


class Rotors(object):
    def __init__(self, AcceptedChars, initialState = [0,0,0]):
        """
        :param initialState:
        :param AcceptedChars: All the chars that can be passed through the rotors
        """
        self.AcceptedChars = AcceptedChars
        self.rotors = []
        for state in initialState:
            self.rotors.append(Rotor(state, AcceptedChars))


    def letter_to_num(self, letter):
        return self.AcceptedChars.index(letter)

    def num_to_letter(self, num):
        return self.AcceptedChars[num]

    def updateRotorStates(self, num=1):
        """
        Update the rotors by the amount given in
        :param num:
        :param reverse:
        :return: None
        """
        # Update their state
        # the first rotor always turns
        completedTurn = True
        for rotor in self.rotors:
            if completedTurn:
                # Update the next rotors state
                completedTurn = rotor.increment_state_and_alert(num)

    def passThroughRotors(self, letter, reverse=False, decypher = False):
        """
        When going through it backwards update the state
        :param letter:
        :return:
        """
        # Turn the letter into a num
        num = self.letter_to_num(letter)


        if reverse:
            #Iterate through them backwards
            for i in range(len(self.rotors)-1, -1, -1):
                #Pass through the number
                rotor = self.rotors[i]

                num = rotor.passThroughRotor(num, decypher)

            if decypher:
                #Update them to go back 1
                self.updateRotorStates(-1)
            else:
                self.updateRotorStates(1)


            #Otherwise don't need to

        else:
            for rotor in self.rotors:
                #Pass thorugh the number
                num = rotor.passThroughRotor(num, decypher)

            #If not decyphering update the state with default vals
            # if decypher == False:
            #     self.updateRotorStates()


        #convert back to letter
        return self.num_to_letter(num)


class Rotor(Rotors):
    def __init__(self, initialState, AcceptedChars):
        """
        Defines an individual rotor
        :param initialState: num on where to start the cipher
        """
        self.state = initialState
        self.AcceptedChars = AcceptedChars
        #From parent class
        self.cipher = self.create_rand_ints()

    def create_rand_ints(self):
        """
        :return:
        """
        result =  []
        for i in self.create_rand_alphabet():
            result.append(self.letter_to_num(i))

        return result

    def letter_to_num(self, letter):
        return self.AcceptedChars.index(letter)

    def create_rand_alphabet(self):
        """
        :return: A list with the order of the acceptable chars randomly scrambled,
        then assigned to the self.alphabet of a rotor
        """
        temp = self.AcceptedChars.copy()
        random.shuffle(temp)
        return temp

    def increment_state(self, num=1):
        #Need 95 to be a number that is possible too
        self.state = (self.state + num) % len(self.cipher)

    def increment_state_and_alert(self, num=1):
        self.increment_state(num)
        #If the cipher has gone through one full rotation return True
        return self.state == len(self.cipher)


    def passThroughRotor(self, num, decypher = False):
        """
        Takes the letter and passes through the rotor
        :param num: The num that is passed through
        :param reverse:
        :return:
        """
        #If passing through it backwards

        #the same going back and forth.
        if decypher:
            #Return the number that was inputted to get the cipher passed in
            #The state is added on input
            input = self.cipher.index(num) - self.state
            if input < 0:
                #In case the number is negative add length of cipher
                return input + len(self.cipher)
            return input
        # if reverse:
        #     #When going backwards get the index of where that number is in the cipher
        #     #So the place its passed in is where num would usually o through +/- (doesn't matter as long as you're consistent) the state of the cipher
        #     return self.cipher.index(num - self.state)
            #Modulus of cipher length to ensure don't go out of range
            #return self.cipher[(num - self.state) % len(self.cipher)]

        #Add the state and return the ouptut all values of cypher are withing range
        return self.cipher[(num + self.state) % len(self.cipher)]


class Enigma(object):
    def __init__(self, stacker, reflector, acceptedChars, rotors = [0,0,0] ):
        """
        :param stacker: dictionary joining two letters together, swaps their values when passed through, unlike enigma won't turn rotors if used.
        :param rotors: List of the initial state of the rotors, you can have any number of rotors.
        """
        self.stacker = stacker
        #Rotors is an object that keeps track of its own state and updates it
        self.rotors = Rotors(acceptedChars, rotors)
        #this should be constant
        self.AcceptedChars = acceptedChars
        self.reflector = reflector

    def get_current_state(self):
        return self.stacker, self.rotors

    def encrypt_message(self, message):
        """
        First passes the message through the stacker,
        then through the rotors
        then through the reflector
        then through the rotors again (their position will have been updated)
        :param message: Message can be any values
        :return: The encrypted message
        """
        result = []
        #First pass it through the steckerbert
        for letter in message:
            stacker_result = self.pass_through_stacker(letter)
            rotor_result = self.rotors.passThroughRotors(stacker_result)
            reflector_result = self.passThroughReflector(rotor_result)
            #Go through it backwards
            rotor_result = self.rotors.passThroughRotors(reflector_result, True)
            result.append(rotor_result)

        return "".join(result)

    def decrypt_message(self, message):
        #Might need to peel back state once for first decrpted letter
        result = []
        #Need to go through the message backwards for the state
        #Need to go back one at the beginning as at the end of the last decryption will have been turned
        self.rotors.updateRotorStates(-1)
        for i in range(len(message)-1,-1,-1):
            letter = message[i]
            # Go through rotors backwards - when decrypting updates state by -1 at end for you
            rotor_result = self.rotors.passThroughRotors(letter, False, True)
            reflector_result = self.passThroughReflector(rotor_result, True)
            #going through it backwards
            rotor_result = self.rotors.passThroughRotors(reflector_result, True, True)
            #Going through it backwards
            stacker_result = self.pass_through_stacker(rotor_result)
            #Insert it at the beginning of the list
            result.insert(0, stacker_result)
        return "".join(result)


    def pass_through_stacker(self, letter):
        """
        :param letter:
        :return: Passes through the stacker, returns letter that it is changed to, the stacker consists of letters paired together such that if one letter is called the other is returned
        otherwise prints error.
        """
        #check if its a key
        try:
            return self.stacker[letter]
        except:
            # Get the values
            for tup in self.stacker.items():
                if tup[1] == letter:
                    return tup[0]

            #The letter isn't in the stacker
            return letter


    def passThroughReflector(self, letter, reversed = False):
        """
        :param letter:
        :param reversed: if true simulates passing through reflector backwards (decryption)
        :return: Passes through the reflector, returns letter that it is changed to,
        otherwise prints error.
        """
        if reversed:
            # Get the values
            tup_dicts = self.reflector.items()
            for tup in tup_dicts:
                if tup[1] == letter:
                    return tup[0]

            print(f"Invalid letter {letter} passed in")


        else:
            try:
                return self.reflector[letter]
            except:
                print(f"Invalid letter {letter} passed in")



#Test the machine
if __name__ == '__main__':
    enigma = Enigma(Stacker, Reflector, AcceptedChars, [10, 35, 77, 19, 0])
    example_message = "Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz This is a cool message isn't it??????"
    example_message_encrypted = "cVuOeBp7qKD$Wo=Zh@qx3@!vYj0v;_I^;Oe+kC dgmgsa{]xR;Y,>-mS+<oMDt>3$-"

    mes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Messages longer than that don't work
    mes_encrypt = enigma.encrypt_message(example_message)
    mes_decrypt = enigma.decrypt_message(mes_encrypt)
    print(mes_encrypt)
    print(mes_decrypt)




#
# machine = Enigma(rand_dict, [20, 11])
#
# print(machine.get_current_state())
#
# # GET USER INPUT
# plainText = input("Please enter our text: ")
# choice  = input("Enter e to encrypt or d to decrypt: ")
#
# if choice == "e":
#     print(machine.encrypt_message(plainText))
# else:
#     print(machine.decrypt_message(plainText))
#
# #mzobjutqlxrhndgec pikafwvys
# #abcdefghijklmnopqrstuvwxy z
# #ABCDEFGHIJKLMNOPQRSTUVWXYZ


