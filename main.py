string = input("Write your input value: ").upper()
morse_dict_alpabet = {
    'A':	'.-',	
    'B': '-...'	,
    'C':	'-.-.',
    'D':	'-..',	
    'E':	'.',	
    'F'	:'..-.',
    'G':	'--.',
    'H':	'....',
    'I':	'..',
    'J':	'.---',
    'K':	'-.-',	
    'L':	'.-..',
    'M':	'--',
    'N':	'-.',
    'O':	'---',
    'P':	'.--.',
    'Q':	'--.-',
    'R':	'.-.',
    'S':	'...',
    'T':	'-'	,
    'U':	'..-',
    'V':	'...-',
    'W':	'.--',
    'X':	'-..-',
    'Y':	'-.--',
    'Z':	'--..'
}

morse_number ={
    '0':	'-----',
    '1':	'.----',
    '2':	'..---',
    '3':	'...--',
    '4':	'....-',	
    '5':	'.....',
    '6':	'-....',
    '7':	'--...',
    '8':	'---..',
    '9':	'----.'
}

final_morse_message = []

for letter in string:
    if letter in morse_dict_alpabet:
        final_morse_message.append(morse_dict_alpabet[letter])
    elif letter in morse_number:
        final_morse_message.append(morse_number[letter])
    else:
        final_morse_message.append(" ")
        
message = " ".join(final_morse_message)
print(message)
