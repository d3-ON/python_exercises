def run():
    age = int(input('Enter your age: '))
    amount = int(input('Enter the amount of articles buying: '))

    if age > 18 and amount > 1:
        print(True)
    else:
        print(False)



if __name__ == '__main__':
    run()
