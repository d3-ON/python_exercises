def run():
    text = input('Enter a text: ')
    print(text[0])
    number = int(input(f'Enter a number between 0 and {len(text)}: '))
    index = 0

    if number > 0 and number < len(text):
        index = number
    else:
        print('The number is wrong')
        run()

    print(text[index])


if __name__ == '__main__':
    run()
