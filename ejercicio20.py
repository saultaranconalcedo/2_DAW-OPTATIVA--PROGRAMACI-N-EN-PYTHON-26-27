duracion_segundos = 7384

horas = duracion_segundos // 3600
minutos_restantes = (duracion_segundos % 3600) // 60
segundos_restantes = duracion_segundos % 60

print("Horas completas:", horas)
print("Minutos restantes:", minutos_restantes)
print("Segundos restantes:", segundos_restantes)
