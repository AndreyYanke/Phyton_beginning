def dan(**kwargs):
    return list(kwargs.values())


print(dan(name = input('Имя: '), surname=input('Фамилия: '), date=input('Год рождения: '),
          town=input('Город проживания: '), email=input('Ваш email: '), tel=input('Ваш номер телефона: ')))
