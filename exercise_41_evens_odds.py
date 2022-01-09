def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def run():
    even = 0
    odd = 0

    for i in range(4):
        n = int(input('Enter a number: '))
        
        if is_even(n):
            even += n
        else:
            odd += n
            
    print(f'Sum of evens: {even}')
    print(f'Sum of odds: {odd}')
    

if __name__ == '__main__':
    run()