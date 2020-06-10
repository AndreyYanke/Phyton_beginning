name = input('Введите имя: ')
suname = input('Введите фамилию: ')
age = input('Ваш вазраст :')
if age.isdigit():
    print('Добрый день, ' + name + ' ' + suname + ' ' + str(age) + ' лет')
else:
    print('Возраст необходимо ввести цифрами')

