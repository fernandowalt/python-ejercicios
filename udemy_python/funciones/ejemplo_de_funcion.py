precios_cafe = [("capuchino", 2.5), ("Expresso", 1.2), ("Moka", 1.9)]


def cafe_mas_caro(tupas):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in tupas:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(f"el cafe {cafe} es el mas caro de los disponibles, con un precio de {precio}")
