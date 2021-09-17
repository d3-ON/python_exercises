def run():
    counter = 0
    num_1 = 0
    num_2 = 1

    while counter < 10:
        print(num_1)
        fibo = num_1 + num_2
        num_1 = num_2
        num_2 = fibo
        counter += 1


if __name__ == '__main__':
    run()
