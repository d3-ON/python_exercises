def run():
    num_1, num_2 = (int(input('Enter the firts number: ')),
                    int(input('Enter the second number: ')))

    if num_1 > num_2:
        print(f'{num_1} is greater than {num_2}')
    elif num_1 < num_2:
        print(f'{num_1} is smaller than {num_2}')
    else:
        print(f'{num_1} is equal than {num_2}')

if __name__ == '__main__':
    run()
