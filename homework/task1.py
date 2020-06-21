def simple_calc():
    work_hour = input('Введите количетсво отработанных часов: ')
    bid_per = input('Введите ставку в час: ')
    prize = input('Введите размер премии: ')
    work_hour = int(work_hour)
    bid_per = int(bid_per)
    prize = int(prize)
    return work_hour * bid_per + prize

import task1
print(task1.simple_calc())