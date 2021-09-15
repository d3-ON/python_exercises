def run():
    name_1 = input('Enter the firts name: ')
    name_2 = input('Enter the second name: ')

    if name_1[0] == name_2[0] or name_1[len(name_1) - 1] == name_2[len(name_2) - 1]:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    run()
