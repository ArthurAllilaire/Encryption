import random


def mirrorAlongCenter(message):
    reversed = ""
    for index in range(len(message)-1,-1, -1):
        reversed += message[index]

    return reversed

def createMirrorList(axis_num, ub = 100, lb = 2):
    """
    :param axis_num: Number of axises to be generated
    :param lb: The lower bound of the axis number
    :param ub: The upper bound (should be about 1/3 the length of the string)
    :return: A list of len = axis_num randomly chosen ints
    """
    result = []
    for i in range(axis_num):
        result.append(random.randint(lb, ub))

    return result

#print(createMirrorList(10))

def splitString(message, window_size, reversed = False):
    """
    Splits a string into a list with each value being a slice of the string with length window_size
    :param window_size:
    :param reversed: defaults to False if true then returns the split string with same values that would have been before
    :return: List with each value with window size slice of string
    """
    result = []
    #GEt the length of the remainder
    remainder = len(message) % window_size
    if reversed and remainder:
        # Need to remove the remainder which will always be one window from the end
        #GEt the remainder
        remainder_str = message[-(remainder+window_size) : -window_size]
        #Remove the remainder as will be added to the list
        message = message[:-(remainder+window_size)] + message[-window_size:]

    # Go through list backwards and append the value to result
    current_index = 0
    for index in range(window_size, len(message)+1, window_size):
        result.append(message[current_index: index])
        current_index = index

    # Add the remainder if there is one
    if remainder:
        if reversed:
            result.insert(-1, remainder_str)
        else:
            result.append(message[-remainder:])

    return result


def mirrorAlongNumber(message, axis_num, reverse = False):
    """
    The message is mirrored over num of axises + 1 for remainders
    :param message: The message you want to decrypt this message
    :param axis_num: should be less than half of message
    :param reverse: Bool specifying whether the message should be reversed engineered
    :return: The mirrored message
    """
    if axis_num == 1:
        return mirrorAlongCenter(message)
    elif axis_num > len(message)/2:
        #There is a limit to how many times the string can be mirrored, each step has to be more than two.
        axis_num = len(message)//2
    window_size = len(message)//axis_num
    split_string = splitString(message, window_size, reverse)

    if reverse:
        for i in range(len(split_string) - 2, -1, -1):
            # Mirror the strings
            last_window = mirrorAlongCenter(split_string[i + 1])
            window = mirrorAlongCenter(split_string[i])

            # Swap the indexes
            split_string[i] = last_window
            split_string[i + 1] = window

        return "".join(split_string)

    # Go through the list
    for i in range(1,len(split_string)):
        #Mirror the strings
        last_window = mirrorAlongCenter(split_string[i-1])
        window = mirrorAlongCenter(split_string[i])

        #Swap the indexes
        split_string[i] = last_window
        split_string[i-1] = window

    return "".join(split_string)

def mirrorStringNtimes(message, axis_nums, reverse=False):
    """
    :param message: The message to be mirrored
    :param axis_nums: list of axis to mirror along, the same that was used to encrypt
    :return: The mirrored string
    """
    #Reverse the order of operations if unmirroring a string
    if reverse:
        axis_nums.reverse()

    for axis_num in axis_nums:
        message = mirrorAlongNumber(message, axis_num, reverse)

    return message


# The below works
# print(mirrorAlongNumber("12345678910;ht;kant;lajsdht;al", 10))
# print(mirrorAlongNumber("654987;01;thnakl;tsjathdla;321", 10, True))

#this works as well
if __name__ == '__main__':
    while True:
        plainText = input("Please enter text: ")
        choice = input("e or d to encrypt or decrypt (anything else to exit): ")

        if choice == "e":
            output = mirrorStringNtimes(plainText, [10,4,15,34,2,3, 15])

        elif choice == "d":
            output = mirrorStringNtimes(plainText, [10,4,15,34,2,3, 15], True)


        else:
            break

        print(output)


#Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz This is a cool message isn't it??????
#llo zy??? Wo t'?He l?nsidqY?tijcbafeeihgSR mUTssaega sv sic  ZpoxwMLKXWV!dQJIHEDCPONGFnBA tihmlkrsrlTuoo
