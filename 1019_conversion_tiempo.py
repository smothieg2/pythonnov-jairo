duracion_segundos = int(input())

horas = duracion_segundos // 3600
minutos = (duracion_segundos % 3600) // 60
segundos = duracion_segundos % 60

print("{}:{}:{}".format(horas, minutos, segundos))
