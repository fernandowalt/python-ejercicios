def contar_primos(numero):
    primos = []

    for num in list(range(2, numero + 1)):
        probable = []
        
        for num2 in list(range(1, num + 1)):
            if num % num2 == 0:

                probable.append(num)
                if len(probable) > 2:
                    break

        if len(probable) == 2:
            primos.append(num)

    return primos


print(contar_primos(100))
