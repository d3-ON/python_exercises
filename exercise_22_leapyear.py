def run():
    year = int(input('Enter a year: '))

    if year % 4 == 0:
        if year % 100 != 0:
            print(f'{year} is an leap-year')
        else:
            if year % 400 == 0:
                print(f'{year} is an leap-year')
            else:
                print(f'{year} is not a leap-year')
    else:
        print(f'{year} is not a leap-year')
        


if __name__ == '__main__':
    run()
