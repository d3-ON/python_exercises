def run():
    stop = False
    prime_number = 0
    
    while stop == False:
        number = input('Enter a number: ')
        prime = True

        if number[0] == '9':
            stop = True
        else:
            for i in range(2, int(number)):
                if int(number) % i == 0:
                    prime = False
            
            if prime == True:
                prime_number += 1
                    
    print(prime_number)

if __name__ == '__main__':
    run()