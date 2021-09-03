def run():
    mi_lista = ["Hola ", "mundo"]
    mi_diccionario = {"nombre": "Humberto","apellidos":"Zapata León"}

    # print('-'.join(mi_lista))

    # nombre = ''
    # for key, value in mi_diccionario.items():
    #     nombre += ','.join(value)
    #     nombre += ' '
    # print(nombre)

    # Obtener de una API los alumnos egresados de la generación 2014
    alumnos_db = [
        {"id_alumno": 2345, "nombre": "Agapito", "apellido_pat": "López", "apellido_mat": "López", "id_estatus":"5"},
        {"id_alumno": 2346, "nombre": "Agapito", "apellido_pat": "López", "apellido_mat": "López", "id_estatus":"5"},
        {"id_alumno": 2347, "nombre": "Agapito", "apellido_pat": "López", "apellido_mat": "López", "id_estatus":"5"},
        {"id_alumno": 2348, "nombre": "Agapito", "apellido_pat": "López", "apellido_mat": "López", "id_estatus":"5"},
    ]

    # for alumno in alumnos_db:
    #     for campo_db, valor in alumno.items():
    #         print(valor)




    # diccionario_numeros = {
    #     "numeros_naturales": [1,2,3,4,5,6,7,8],
    #     "numeros_enteros": [1,-4,0,56],
    #     "numeros_flotantes": [1.1,4.5,6.7]
    # }

    # for nombre_lista, valores_lista in diccionario_numeros.items():
    #     nueva_lista = list(valores_lista)
    #     nueva_lista.append(100)
    #     diccionario_numeros[nombre_lista] = nueva_lista
    # print(diccionario_numeros)



    historial = [
        {
            "cuatrimestre_1": [
                {"Asignatura": 1},
                {"Asignatura": 2},
                {"Asignatura": 3},
                {"Asignatura": 4},
                {"Asignatura": 5},
            ]
        },
    ]
    print(historial)





if __name__ == '__main__':
    run()