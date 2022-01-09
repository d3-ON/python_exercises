def enter_num():
    num = int(input('Enter the amount money: '))
    
    return num




def run():
    stop = False
    total = 0
    
    while stop == False:
        amount = enter_num()
        
        if amount > 0:
            total += amount
        elif amount < 0:
            enter_num()
        elif amount == 0:
            stop = True

             
        
    print(f'The total amount is {total}')


if __name__ == '__main__':
    run()