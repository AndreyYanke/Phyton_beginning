a =input('Введите число: ')
a= int(a)
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
        a = a // 10
    print("Максимальное цифра в числе: " + str(m))
    break
