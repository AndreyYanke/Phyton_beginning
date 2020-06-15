user = input('Введите несколько слов: ')
word = []
num = 1

for elem in range(user.count(' ') + 1):
    word = user.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [elem]}")
        num += 1
    else:
        print(f" {num} {word [elem] [0:10]}")
        num += 1