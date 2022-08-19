# from random import shuffle

# palitos = ["-", "--", "---", "----"]

# def mezclar_palitos(lista):
#     shuffle(lista)
#     return lista

# def probar_suerte():
#     intento = 0
#     while intento not in range(1, 5):
#         intento = int(input("elige un numero del 1 al 4: "))

#     return intento

# def comprobar_intento(lista: list[str], intento: int):

#     if lista[intento - 1] == "-":
#         print("perdiste, ahora te toca lavar los platos")
#     else:
#         print("esta vez te has salvado")

#     print(f"tu eleccion fue {lista[intento-1]}")

# comprobar_intento(mezclar_palitos(palitos), probar_suerte())

# 2.ejercicio lanzar dados


# from random import randint


# def lanzar_dados():

#     return [randint(1, 6), randint(1, 6)]


# def evaluar_jugada(d1, d2):
#     suma_dados = d1 + d2
#     texto = ""

#     match suma_dados:
#         case suma_dados if suma_dados <= 6:
#             texto = f"La suma de tus dados es {suma_dados}. Lamentable"
#         case suma_dados if suma_dados > 6 and suma_dados < 10:
#             texto = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#         case suma_dados if suma_dados >= 10:
#             texto = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#     return texto


# dado1, dado2 = lanzar_dados()
# evaluar_jugada(dado1, dado2)

# from random import randint


# def lanzar_dados():

#     return [randint(1, 6), randint(1, 6)]


# def evaluar_jugada(d1, d2):
#     suma_dados = d1 + d2
#     texto = ""

#     if suma_dados <= 6:
#         texto = f"La suma de tus dados es {suma_dados}. Lamentable"
#     elif suma_dados > 6 and suma_dados < 10:
#         texto = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#     elif suma_dados >= 10:
#         texto = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#     return texto


# dado1, dado2 = lanzar_dados()
# print(evaluar_jugada(dado1, dado2))


# lista_numeros = [1, 2, 15, 7, 2]


# def reducir_lista(lista):
#     nueva_lista = []
#     numero_maximo = max(lista)
#     for num in lista:
#         if num in nueva_lista or num == numero_maximo:

#             continue
#         else:
#             nueva_lista.append(num)
#     return nueva_lista


# def promedio(lista):
#     return sum(lista) / len(lista)


# promedio(reducir_lista(lista_numeros))

from random import randint

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def lanzar_moneda():
    return ["Cara", "Cruz"][randint(0, 1)]


def probar_suerte(resultado_moneda, lista):

    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        del lista[:]

    return lista


probar_suerte(lanzar_moneda(), lista_numeros)
