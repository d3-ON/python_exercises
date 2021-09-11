def run():
    num_1, num_2 = int(input('Enter a number 1: ')), int(input('Enter a number 2: '))
    sum = num_1 + num_2
    print(f'The result of the sum is {sum}')
    num_3 = int(input('Enter a number 3: '))
    print(f'The result of the operation is {sum * num_3}')


if __name__ == '__main__':
    run()
