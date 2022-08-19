# def suma(**kwargs):

#     total = sum(kwargs.values())
#     for clave, valor in kwargs.items():
#         print(f" la  clave {clave} tiene el valor {valor}")

#     return total


# print(suma(x=3, y=5, z=2))


# def cantidad_atributos(**kwargs):

#     return len(kwargs)


# print(cantidad_atributos(a=5, b=12, c=30))


# def lista_atributos(**kwargs):
#     lista = []

#     for key, val in kwargs.items():
#         lista.append(val)

#     return lista


# print(lista_atributos(a=10, c=80, d=25))


# def describir_persona(nombre, **kwargs):

#     print(f"características de {nombre}:")

#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")


# def devolver_distintos(a, b, c):
#     numeros = [a, b, c]
#     numeros_ordenados = sorted(numeros)
#     suma = sum(numeros_ordenados)
#     if suma > 15:
#         return numeros_ordenados[2]
#     elif suma < 10:
#         return numeros_ordenados[0]
#     elif suma in range(10, 15):
#         return numeros_ordenados[1]


# print(devolver_distintos(5, 2, 6))


# def ordenar_palabras(palabra):
#     lista_palabra = list(palabra.lower())
#     palabra__ordenada_filtrada = sorted(list(set(lista_palabra)))

#     return palabra__ordenada_filtrada


# print(ordenar_palabras("EstaciOnaMiento"))


# from random import randint


# def numeros_gemelos(*args):
#     numero_anterior = 1
#     print(numero_anterior)

#     for numero in args:
#         if numero == 0 and numero_anterior == 0:
#             return True
#         else:
#             numero_anterior = numero

#     return False


# print(numeros_gemelos(0, 1, 2, 3, 4, 5, 6, 0, 7, 8))


