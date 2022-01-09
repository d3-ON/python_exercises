# 4
# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos 
# por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. 
# Mostrar el consumo de combustible por kilómetro.


def run():
    km = float(input('Enter the kilometers traveled: '))
    fuel = float(input('Enter the amount of fuel consumed: '))
    consume = 1 / (km / fuel)
    print(f'The consume for kilometers is {round(consume, 3)}')


if __name__ == '__main__':
    run()
