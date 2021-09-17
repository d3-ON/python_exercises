def run():
    numbers = [int(input('Enter a number: ')), int(input('Enter a number: ')),
               int(input('Enter a number: ')), int(input('Enter a number: ')),
               int(input('Enter a number: ')), int(input('Enter a number: '))]
    positive = 0
    negative = 0
    counter = 0
    zero = False

    for i in numbers:
        if i > 0:
            positive += i
            counter += 1
        elif i < 0:
            negative += i
        else:
            print('Error: 0 is a wrong number!')
            zero = True
            break;

    if positive > 0 and zero == False:
        print(f'The average of positive is {positive/counter}')

    if negative < 0 and zero == False:
        print(f'The sum of nevative numbers is {negative}')


if __name__ == '__main__':
    run()
