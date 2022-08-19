# def suma(*args):
#     # *args retorna una tupla de todos los argumentos

#     # luego, dado que una tupla es un iterable le aplicamos el metodo sum() y este retorna el valor de la suma
#     return sum(args)


# print(suma(1, 5, 6, 1))


# def suma_cuadrados(*numeros):
#     resultado = 0
#     for num in numeros:
#         resultado += num**2
#     return resultado


# print(suma_cuadrados(2, 5, 1))


# def suma_absolutos(*args):
#     total = 0
#     for num in args:
#         if num < 0:
#             num = num * -1
#             total += num
#         else:
#             total += num

#     return total


# print(suma_absolutos(-5, -2, 10, 6, -4, -2))


def numeros_persona(nombre, *numeros):
    total = 0
    for num in numeros:
        if num < 0:
            num = num * -1
            total += num
        else:
            total += num

    return f"{nombre}, la suma de tus números es {total}"

print(numeros_persona('walter',10,-10,50,-50))
