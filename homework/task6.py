from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

it = int(input('Сколько раз повторить элементы списка? '))
a = ["ABC", 1, 5, 'dog']
c = 0
for el in cycle(a):
    if c >= it:
        break
    print(el)
    c += 1