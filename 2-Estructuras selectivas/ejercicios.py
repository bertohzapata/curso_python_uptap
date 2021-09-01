# 1-Solicita al usuario el promedio de un alumno (1-100)
# y si el alumno obtiene al menos 70, indica que pasa al siguiente 
# cuatrimestre, de lo contrario indica que ha reprobado
# promedio = int(input("Dame el promedio del alumno: "))
# if promedio >= 70:
#     print('Alumno aprobado')
# else: 
#     print('Alumno reprobado')

#2- Solicita la edad de un cliente de cine y delimitar el precio de
# su entrada. Si tiene menos de 5 años su acceso es gratis, de 5 a 59
# para la tarifa normal (80) y si tiene de 60 en aledante para una tarifa
# reducida (40)
edad_cliente = int(input("Edad cliente: "))
edadCliente2 = 9

if edad_cliente < 5:
    print('La entrada es gratis')
elif edad_cliente >=5 and edad_cliente < 60:
    print('La tarifa es de 80')
else:
    print('La tarifa es de 40')