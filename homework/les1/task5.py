revenue = input('Введите Вашу выручку: ')
cost = input('Введите Ваши издержки: ')
revenue = int(revenue)
cost = int(cost)


if revenue > cost:
    profit = revenue - cost
    profitability = (profit / revenue)
    print('Вы отработали с положительным финансовым показателем, '
          'Ваша прибыль составляет: {0} рублей.\nВаша рентабильность составила: {1:=2} рублей.'.format(profit, round(profitability, 2)))
    if revenue > cost:
        number_of_workers = input('Введите количество работников: ')
        number_of_workers = int(number_of_workers)
        profit_per_workers = profit / number_of_workers
        print('Прибыль на одного сотрудника составляет: ' + str(profit_per_workers) + ' рублей' )
else:
    loss = cost - revenue
    print('Вы отработали в убыток, Ваш убыток составляет: ' + str(loss))


