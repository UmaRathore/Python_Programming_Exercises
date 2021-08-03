# Rotational Cipher
# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount.
# Rotating a character means replacing it with another character that is a certain number of steps away
# in normal alphabetic or numerical order.
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?".
# Every alphabetic character is replaced with the character 3 letters higher (wrapping around
# from Z to A), and every numeric character replaced with the character 3
# digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
# Given a string and a rotation factor, return an encrypted string.


def rotationalCipher(input_str, rotation_factor):

    dict_alphabets = {

        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'P': 16,
        'L': 12
    }

    output = ""
    char_str = 0

    while char_str < len(input_str):

        str_char = input_str[char_str]
        if input_str[char_str] in dict_alphabets.keys():
            output += check_alphabet(dict_alphabets, input_str[char_str], rotation_factor)
        elif str_char.isdigit():
            nex_num = int(str_char) + rotation_factor
            output += str(nex_num)
        else:
            output += input_str[char_str]
        char_str += 1

    return output


def check_alphabet(dict_letters, val, rotation):

    index = 0
    new_letter = ""
    for key, value in dict_letters.items():
        if val == key:
            index = int(value) + rotation

    for key, value in dict_letters.items():
        if value == index:
            new_letter = key

    return new_letter


print(rotationalCipher('A-B*C#12@', 2))
