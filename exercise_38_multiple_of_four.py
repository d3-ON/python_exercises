# 38
# Escribí un programa que solicite al usuario una cadena de caracteres 
# (que puede contener letras, números o símbolos). Analizar la cadena para mostrar: cuántas letras del abecedario 
# (minúsculas y mayúsculas) contiene, cuántos símbolos (caracteres que no son ni letras ni números), cuántos dígitos 
# numéricos y, de los dígitos, cuántos son múltiplos de 4.


def run():
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y',
    'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z']
    CHARS = ['*', '+', '-', '/', '@', '_', '?',
    '!', '[', '{', '(', ')', '}', ']', ',', ';',
    '.', '>', '<', '~', '°', '^', '&', '$', '#',
    '"', '=', '¡', ' ']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    letter_count = 0
    num_count = 0
    chars_count = 0
    container = ''
    multiple = 0
    sentence = input('Enter a word: ')

    
    for i in sentence:
        for indx in LETTERS:
            if i == indx: 
                letter_count += 1
                
        for indx in CHARS:
            if i == indx:
                chars_count += 1
            
        for indx in NUMS:
            if i == indx:
                num_count += 1
                if int(i) % 4 == 0:
                    multiple += 1
                
    print(f'Amount of letters: {letter_count}')
    print(f'Amount of numerical digits: {num_count}')
    print(f'Amount of symbols: {chars_count}')
    print(f'Amount of multiple: {multiple}')                             
                                    

if __name__ == '__main__':
    run()