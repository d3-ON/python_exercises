def run():
    num_1, num_2, num_3 = (int(input('Enter the firts name: ')),
                           int(input('Enter the second name: ')),
                           int(input('Enter the firts name: ')))

    if (num_1 < num_2 and num_1 < num_3):
        print(f'{num_1} is smaller')
    elif num_2 < num_3:
        print(f'{num_2} is smaller')
    elif num_3 < num_2:
        print(f'{num_3} is smaller')
    else:
        print('all numbers are equal')


if __name__ == '__main__':
    run()
