def run():
    number = int(input('Enter a number: '))

    if number > 0:
        print(f'The valor absolute of {number} is {number}')
    elif number < 0:
        print(f'The valor absolute of {number} is {number * -1}')


if __name__ == '__main__':
    run()
