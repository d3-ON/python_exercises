def run():
    letter = input('Enter only one letter: ')
    VOWEL = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u',]

    if len(letter) == 1:
        for i in VOWEL :
            if letter == i:
                print(f'{letter} is a vowel')
    else:
        print('You entered more than two letters')



if __name__ == '__main__':
    run()
