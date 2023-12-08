# Morse Code Translator

# Setup
# Data Mapping
# User Input
# Translation
# Output

# Dictionary for Morse Code
englishToMorse = {
        # Alphabet
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': ' ',

}
# Get user input
userString = input("Enter a random english text: ")

# Write a function to translate the text based on user choice
def translate(text):
        # convert text into uppercase
        text = text.upper()
        morseString = ""
        return text

# Show translated text to the user
print(translate(userString)) 