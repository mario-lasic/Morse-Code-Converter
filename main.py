# Morse code dictionary
morse_code_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

# Getting user input
user_input = input("Write something you want to encrypt: ")


# Function that convert normal string to morse code
def converter(input):
    encrypted_input = ""
    for char in input:
        if char == " ":
            encrypted_input += "       "
        elif char.upper() in morse_code_dict.keys():
            encrypted_input += morse_code_dict[char.upper()]
            encrypted_input += "  "
        else:
            continue

    return encrypted_input


# Prints encrypted string
print(converter(user_input))
