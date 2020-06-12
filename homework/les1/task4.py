n = input("Введите целое положительное число ")
n = int(n)
max = 0

while n >= 0:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break