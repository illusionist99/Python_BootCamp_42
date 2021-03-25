import sys

morse_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def check_param(params):
    for argm in params:
        for letter in argm:
            if not (letter.isalnum() or letter.isspace()):
                return -1
    return 0




def print_morsed(msg):
    for i in range(len(msg)):
        if msg[i].upper() in morse_dict:
            print(morse_dict[msg[i].upper()], end='')
        if i != len(msg) - 1:
            print(" ", end='')


args = sys.argv[1:]
if check_param(args) == -1:
    print("ERROR")
    exit(-1)

for arg in args:
    print_morsed(arg)
    if arg != args[-1]:
        print(" / ", end='')

print("")
