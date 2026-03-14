def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]


# exemplo de execução
numeros = [10, 20, 30, 40]

resultado = verificar_primeiro(numeros)

print("Primeiro elemento:", resultado)
