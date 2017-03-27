ascii_a = 97
ascii_A = 65


def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - ascii_A
    elif letter.islower():
        return ord(letter) - ascii_a
    else:
        return letter

		
#print(alphabet_position("a"))  # test
#print(alphabet_position("@"))  # test

		
def rotate_character(char, rot):
    char_pos = alphabet_position(char)
#    print(char_pos)  # test

    if char.isupper():
        rotated_char = (char_pos + rot) % 26 + ascii_A
        return chr(rotated_char)

    elif char.islower():
        rotated_char = (char_pos + rot) % 26 + ascii_a
        return chr(rotated_char)

    else:
        return char

		
#print(rotate_character("a", 13))  # test