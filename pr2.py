login = input("Введите логин : ")
password = input("Введите пароль : ")

with open('C:\Python\слайды\log.txt', 'a') as file:
    file.write(login + ' ' + password + '\n')