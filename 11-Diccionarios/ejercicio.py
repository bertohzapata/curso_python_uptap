# A partir de un diccionario con 3 materias definidas
# Solicita al usuario las calificaciones
# y muestra los resultados de calificación por materia
# así como su promedio

# materias = {"Programación web": 0, "Bases de datos": 0, "Fundamentos de prog.": 0}
# materias["Programación web"] = 10



materias = {"Programación web": 0, "Bases de datos": 0, "Fundamentos de prog.": 0}

promedio = 0
print(materias)
for materia, calificacion in materias.items():
    cal = int(input(f'Dame el valor de la materia {materia} - '))
    materias[materia] = cal
    promedio += cal
promedio = round((promedio/3),2)
print(materias)
print("Promedio:",promedio)