def run():
    shows = int(input('How many musical shows have you seen in the last year? '))
    if shows < 3:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    run()
