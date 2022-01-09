def sum_of_digits(n):
    sum = 0
    
    for i in list(n):
        sum += int(i)
        
    return sum 

def run():
    n = input('Enter a number: '
              )
    while n != '100':
        sum = sum_of_digits(n)
        
        print(sum)
        
        n = input('Enter a number: ')


if __name__ == '__main__':
    run()