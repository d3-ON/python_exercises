# 2
# Escribí un programa que solicite al usuario ingresar un número con decimales y 
# almacenalo en una variable. A continuación, el programa debe solicitar al usuario que 
# ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá 
# guardar el resultado de la suma de los dos números ingresados por el usuario. Por último,
# se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” 
# se reemplazará por el resultado de la operación.
 


num_1 = float(input('Enter a decimal number: '))
num_2 = int(input('Enter a int number: '))
sum = num_1 + num_2
print(F'The result of the sum is {sum}')
