from functools import reduce

number = ([num for num in range(100, 1000) if num % 2 ==0])

print(reduce(lambda x, y: x * y, number))
