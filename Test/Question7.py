#7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#Примеры:
#1234565 seconds = 14:6:56:5

sec = 56723578264928
min = sec/60
hour = min/60
day = hour/24
hour_print = int(hour % 24)
min_print = int(min % 60)
sec_print = int(sec % 60)

print(f'{int(day)}:{int(hour_print)}:{min_print}:{sec_print}')