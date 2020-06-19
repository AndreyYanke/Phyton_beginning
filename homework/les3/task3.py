'''Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.'''

def my_func(a, b, c):
     result = [a, b, c]
     result.remove(min(a,b,c))
     return sum(result)

print(my_func(2, 15, 8))


