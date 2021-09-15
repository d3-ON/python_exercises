def run():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user_validation = 'Gwenevere'
    pass_validation = 'excalibur'

    if username == user_validation:
        if password == pass_validation:
            print('User and password are correct, you can enter camelot')
        else:
            print('The password it´s incorrect')
    else:
        print('The username it´s incorrect')


if __name__ == '__main__':
    run(),
