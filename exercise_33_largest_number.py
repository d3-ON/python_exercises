def run():
    number = int
    higher = 0
    
    while number != 0:
        number = int(input('Enter a integer number: '))
        
        if number > higher:
            higher = number
            
    
    print(higher)


if __name__== '__main__':
    run()