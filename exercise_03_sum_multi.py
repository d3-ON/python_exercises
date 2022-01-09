# 3
# Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en 
# una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el 
# resultado de la suma anterior.
 


def run():
    num_1, num_2 = int(input('Enter a number 1: ')), int(input('Enter a number 2: '))
    sum = num_1 + num_2
    print(f'The result of the sum is {sum}')
    num_3 = int(input('Enter a number 3: '))
    print(f'The result of the operation is {sum * num_3}')


if __name__ == '__main__':
    run()
