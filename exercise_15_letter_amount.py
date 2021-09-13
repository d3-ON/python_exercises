def run():
    word_1, word_2 = input('Enter the firts word: '), input('Enter the second word: ')

    if len(word_1) < len(word_2):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    run()
