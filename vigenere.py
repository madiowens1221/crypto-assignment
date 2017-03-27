from helpers import alphabet_position, rotate_character

ascii_a = 97
ascii_A = 65

def encrypt(text, key):
    new_text = ''
    j = 0
    for i in range(0, len(text), 1):
        if ord(text[i]) < ascii_A:
            new_text += text[i]
        else:
            new_text += rotate_character(text[i], alphabet_position(key[j % (len(key))]))
            j += 1
    return new_text


def main():
	from sys import argv
	input_text = str(input("Type a message: "))
	print(encrypt(input_text, argv[1]))

if __name__ == '__main__':
    main()
