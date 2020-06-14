user = input('Введите номер месяца: ')
user = int(user)

my_list = ['winter', 'spring', 'summer', 'autumn']

if user == 1 or user == 2 or user == 12:
    print(my_list[0])
elif user == 3 or user == 4 or user == 5:
    print(my_list[1])
elif user == 6 or user == 7 or user == 8:
    print(my_list[2])
elif user == 9 or user == 10 or user == 11:
    print(my_list[3])
else:
    print('Такого номера месяца нет!')

my_dict = {'wi':'winter', 'sp':'spring', 'su':'summer', 'au':'autumn'}

if user == 1 or user == 2 or user == 12:
    print(my_dict['wi'])
elif user == 3 or user == 4 or user == 5:
    print(my_list['sp'])
elif user == 6 or user == 7 or user == 8:
    print(my_list['su'])
elif user == 9 or user == 10 or user == 11:
    print(my_list['au'])
else:
    print('Такого номера месяца нет!')



