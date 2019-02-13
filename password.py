password = 'a123456'
count = 3

while True:
    user_password = input('Please enter your password: ')
    if user_password == password:
        print('Login succed !')
        break
    else:
        count = count - 1
        if count == 0:
            print('Wrong password, you dont have chance.')
            break
        print('Wrong password, you have ', count, 'chance.')