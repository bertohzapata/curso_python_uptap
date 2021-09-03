# A partir de un diccionario con 3 materias definidas
# Solicita al usuario las calificaciones
# y muestra los resultados de calificación por materia
# así como su promedio

import random

materias = {"Programación web": 0, "Bases de datos": 0, "Fundamentos de prog.": 0}
promedio = 0
print(materias)
for asignatura, calificacion in materias.items():
    calificacion = int(random.random() * 100)
    materias[asignatura] = calificacion
    promedio += calificacion
promedio = round(promedio/len(materias),2)
print(materias)
print("Promedio:",promedio)
if promedio >= 70:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")