def run():
    number = input('Enter a number: ')
    sum_total = 0
    
    for i in list(number):
        sum_total += int(i)
        
    print(sum_total)

if __name__ == '__main__':
    run()