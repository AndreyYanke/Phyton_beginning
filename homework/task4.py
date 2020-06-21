
from random import randint

number_list = [randint(20, 100) for i in range(30)]
print(number_list)
my_list = [el for el in number_list if number_list.count(el) == 1]
print(my_list)

