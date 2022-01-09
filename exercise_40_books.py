def run():
    book = input('Enter the name of a book: ')
    num_count = 0
    line = 0
    
    while book != '*':
        for i in book:
            for indx in range(10):
                if i == str(indx):
                    num_count += 1
        
        if book == '/':
            print(f'appear {num_count} digits in the line')
            line += 1
            num_count = 0
            
        book = input('Enter the name of a book: ')
            
    print(f'{line} complete lines were read')


if __name__ == '__main__':
    run()