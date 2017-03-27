from helpers import alphabet_position, rotate_character

ascii_a = 97
ascii_A = 65

def encrypt(text, rot):
    rotated_text = ''
    for char in text:
        rotated_text += rotate_character(char, rot)
    return rotated_text

#print(encrypt("Hello, World!", 5))  # test



def main():
	from sys import argv
	input_text = str(input("Type a message: "))
	print(encrypt(input_text, int(argv[1])))

if __name__ == '__main__':
    main()