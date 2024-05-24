from playsound import playsound
import time

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def convert_to_morse_code(text):
    morse = []
    for char in text.upper():
        if char in morse_code:
            morse.append(morse_code[char])
        else:
            morse.append(char)
    return ' '.join(morse)

def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            playsound('DOT.wav')
            time.sleep(0.1)
        elif symbol == '-':
            playsound('DASH.wav')
            time.sleep(0.1)
        elif symbol == ' ' or symbol=='/':  
            time.sleep(0.3)
        else:
            # Non-alphanumeric characters
            print("Symbol",symbol,"is invalid Character")

# Messages
text = input("Enter the message which you want to convert in Morse Code: ")
morse_text = convert_to_morse_code(text)
print("\nYour message: ",text)
print("Morse Code: ",morse_text)
play_morse_code(morse_text)

