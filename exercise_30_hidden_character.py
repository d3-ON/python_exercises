def run():
    sentence = input('Enter a sentence: ')
    letter = input('Enter a letter: ')
    phrase = ''

    for i in sentence:
        if i == letter:
            i = '*'
        phrase += i

    print(phrase)

if __name__ == '__main__':
    run()
