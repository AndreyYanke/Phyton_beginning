distance = input('Введите количесво километров которое пробежали: ')
purpose = input('Введите какое количество киллометров хотите пробежать ')
distance = int(distance)
purpose = int(purpose)
day = 1

while distance <= purpose:
    print('{0}-й день: {1}'.format(day, round(distance, 2)))
    distance *= 1.1
    day += 1









