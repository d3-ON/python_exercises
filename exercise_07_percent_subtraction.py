def run():
    num = float(input('Enter a number: '))
    result = abs(((num * 15) / 100) - num)
    print(f'The result is {round(result, 2)}')

if __name__ == '__main__':
    run()
