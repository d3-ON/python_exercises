def run():
    number = input('Enter a number formed for eight digits without rare characters: ')

    if len(number) != 8:
        print('The number of digits is wrong')
    else:
         day = int(number) // 1000000
         month = (int(number) % 1000000) // 10000
         year = int(number) % 10000
         date = f'The date is {day}/{month}/{year}'

    print(date)

if __name__ == '__main__':
    run()
