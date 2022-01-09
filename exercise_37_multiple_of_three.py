def run():
    number = int(input('Enter a number: '))
    multiple_of_three = 0
    
    while number > -1:
        even_digits = 0
        odd_digits = 0
 
        for i in list(str(number)):
            if int(i) % 2 == 0:
                even_digits += 1
            else:
                odd_digits += 1
                
            if int(i) % 3 == 0
                multiple_of_three += 1
        
        print(f'Even digits are: {even_digits}')
        print(f'Odd digits are: {odd_digits}')
        
        number= int(input('Enter a number or enter -1 to end: '))
        
    print(f'Multiples of three are: {multiple_of_three}')      
        
if __name__ == '__main__':
    run()