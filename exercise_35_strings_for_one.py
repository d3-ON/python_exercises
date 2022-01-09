def run():
    letter = input('Enter only a letter: ')
    word = ''
    amount = 0
    a = 0
    
    while len(letter) == 1 and letter != '0':
        word += letter
        amount += 1
        
        if letter == 'a':
            a += 1 
            
        letter = input('Enter only a letter: ')

    a_percent = (a / amount) * 100
    
    print(word)
    print(f'a percent is: {a_percent}')
    
if __name__ == '__main__':
    run()