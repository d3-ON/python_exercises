def run():
    text = input('Enter a text: ')
    VOWEL = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowel_counter = 0

    for i in text:
        for x in VOWEL:
            if i == x:
                vowel_counter += 1

    print(vowel_counter)



if __name__ == '__main__':
    run()
