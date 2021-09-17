def run():
    num = 7
    fact = 0

    for i in range(num + 1):
        fact = fact * i
        if fact == 0:
            fact = 1
            
    print(fact)

if __name__ == '__main__':
    run()
