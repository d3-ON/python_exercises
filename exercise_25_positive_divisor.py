def run():
    number = int(input('Enter a number: '))

    for i in range(1, number):
        if number % i == 0:
            print(i)


if __name__ == '__main__':
    run()
