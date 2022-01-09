def palindrome(word):
    reverse_word = word[::-1]
    
    if reverse_word == word:
        return True
    else:
        return False    

def run():
    stop = False
    palindrome_amount = 0
    
    while stop == False:
        word = input('Enter a word: ')
        
        if palindrome(word):
            palindrome_amount += 1
        
        if word == 'fin' or word == 'FIN':
            stop = True
            
    print(palindrome_amount)     


if __name__ == '__main__':
    run()