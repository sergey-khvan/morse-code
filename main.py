MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    
def encryptor(text):
    encrypted_text = ""
    for char in text.upper():
        if char not in MORSE_CODE_DICT:
            encrypted_text += " _ "
        else:
            encrypted_text+= MORSE_CODE_DICT[char] + ' '
    return encrypted_text

def decryptor(enc_text):
    dec_text = ""
    for char in enc_text.split(' '):
        if char == '_':
            dec_text += ' '
        else:
            for key, value in MORSE_CODE_DICT.items():
                if char==value:
                    dec_text+=key
    return dec_text
        


option = input("Do you want to encrypt of decrypt the code? Enter 0 for encrypt and 1 for decrypt: ")
if option == "0" :
    plain_text = input("Input Text to encrypt: ")
    print(encryptor(plain_text))
elif option == "1":
    enc_text = input("Input the Morse code: ")
    print(decryptor(enc_text))
else:
    print("Incorrect choice.")