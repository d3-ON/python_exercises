from exercise_41_evens_odds import is_even
from exercise_42_sum_digits import sum_of_digits

def run():
    stop = False
    odd = 0
    
    while stop == False:
        n = input('Enter a number: ')
        sum = sum_of_digits(n)
        
        if is_even(int(n)) is False:
            odd += 1
            
        if sum > 1000 or sum % 5 == 0:
            stop = True
                        
        sum = 0 
            
    print(odd)
            

if __name__ == '__main__':
    run()