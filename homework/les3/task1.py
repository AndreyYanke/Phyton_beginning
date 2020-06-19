try:
    a = int(input('Введите число: '))
    b = int(input('Введите число на которое нужно разделить: '))
    c = a/b
    print(round(c, 2))
except ZeroDivisionError:
    print(' На ноль делиьть нельзя')
