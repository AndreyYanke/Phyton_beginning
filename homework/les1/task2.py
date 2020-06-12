sec = input('Введите количество секунд: ')
sec = int(sec)
hour = ((sec//3600))%24
minute = (sec//60)%60
second = sec%60
print('Точное время: ' + '{0:=02}:{1:=02}:{2:=02}'.format(hour, minute, second) )
