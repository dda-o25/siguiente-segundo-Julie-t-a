"""
Julieta Núñez Pacheco
19 de septiembre de 2025
Este ejercicio marca la hora si a la original se 
le suma un segundo
"""

#Entradas

hora=int(input("dame una hora: "))
minutos = int(input("dame un minuto: "))
segundos = int(input("dame una segunos: "))

#Procesos

segundos = segundos + 1
if segundos== 60:
    minutos = minutos + 1
    segundos = 0
else:
    segundos = segundos
if minutos == 60:
    hora = hora+1
    minutos = 0
else:
    minutos = minutos

if hora == 24:
 hora = 0
else:
   hora = hora

#Salidas

print("La hora es: ",hora, ":",
       minutos, ":", segundos)