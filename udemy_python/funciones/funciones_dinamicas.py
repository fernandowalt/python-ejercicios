# def tiene_tres_cifras(numero):
#     return numero in range(100, 1000)


# resultado = tiene_tres_cifras(58)

# print(resultado)


# def tiene_tres_cifras(lista):
#     for n in lista:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass

#     return False


# resultado = tiene_tres_cifras([555, 99, 6000])

# print(resultado)


# def tiene_tres_cifras(lista):
#     correctos = []
#     for n in lista:
#         if n in range(100, 1000):
#             correctos.append(n)
#         else:
#             pass
#     return correctos


# resultado=tiene_tres_cifras([10,55,789,89,471,1455,888])

# print(resultado)


# def todos_positivos(lista):

#     for n in lista:
#         if n < 0:
#             return False
#     return True

# print(todos_positivos([1,2,3,-4,5,6,7,8,9]))

# lista_numeros = [1, 2, 4, 5, -4, -10, 1, 1500, 48500, 25]


# def suma_menores(lista):
#     suma = 0
#     for n in lista:

#         if (n > 0) and (n < 1000):
#             suma = suma + n

#     return suma


# print(suma_menores(lista_numeros))


def cantidad_pares(lista):
    count = 0
    for n in lista:
        if n % 2 == 0:
            count += 1
    return count


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 13, 14, 15]

print(cantidad_pares(lista_numeros))
