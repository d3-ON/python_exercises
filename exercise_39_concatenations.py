# 39
# Escribí un programa que permita al usuario ingresar números que serán leídos como string 
# (no como int o float) hasta que ingrese uno que sea múltiplo de 10 ó menor que 0 (que no será procesado). 
# Se formarán dos strings, en los cuales se concatenarán los números ingresados, 
# según el siguiente criterio: en un string se concatenarán todos los números que el usuario ingrese cuya cantidad 
# de dígitos sea un múltiplo de 3. En el otro, se concatenarán todos los números que contengan el dígito 0. Si un número cumple 
# ambas condiciones, debe concatenarse en ambos strings. En cada string, después de cada número concatenado debe colocarse el carácter “-”. 
# Al finalizar, mostrar en pantalla ambos strings.


def run():
    number = input('Enter a number: ')
    string_1 = ''
    string_2 = ''
    
    while int(number) % 10 != 0 and int(number) > 0:
        if len(number) % 3 == 0:
            string_1 += (number + '-')
        
        for i in number:
            if int(i) == 0:
                string_2 += (number + '-')

        number = input('Enter a number: ')
    
    print(f'Numbers whose amount digits are multiple of 3: {string_1}')
    print(f'Numbers that contain 0: {string_2}')


if __name__ == '__main__':
    run()