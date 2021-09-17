def run():
    fahrenheit = float(input('Enter the temperature: '))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f'The temperature in celsius degrees is {round(celsius, 2)}°')


if __name__ == '__main__':
    run()
