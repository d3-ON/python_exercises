def run():
    num_1, num_2, num_3 = float(input('Enter the firts number: ')), float(input('Enter the second number: ')), float(input('Enter the third number: '))
    average = (num_1 + num_2 + num_3) / 3
    print(f'The average of the numbers is {round(average, 2)}')


if __name__ == '__main__':
    run()
