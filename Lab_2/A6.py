n = int(input('введите сколько прошло секунд: '))
hour = n//(60*60)
minut = (n-hour*60*60)//60
sec = n-hour*60*60-minut*60
print('{}:{:02}:{:02}'.format(hour, minut, sec))