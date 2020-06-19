def result():
	res = 0
	while True:
	   user_number = input('Введите цифры через пробел или # для выхода:  ').split( )
	   for i in user_number:
	   	try:
	   		if i == '#':
	   			print(f'Ваш результа: {res}.')
	   			return
	   		else:
	   			res+=int(i)
	   	except ValueError:
	   		print('Введите число или #: ')
	   print(f' Ваш результат: {res}')

print(result())
