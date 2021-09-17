def run():
    phrase = input('Enter a phrase: ')
    sentence = ''
    counter = 0
    chars_number = len(phrase)

    while counter < len(phrase):
        count = 1
        for i in phrase:
            if count == chars_number:
                sentence += i
                counter += 1
                chars_number -= 1
            count += 1
            
    print(sentence)


if __name__ == '__main__':
    run()
