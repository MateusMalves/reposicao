def encontrar_pares(inicio, fim):
    pares = [] 
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            pares.append(numero)
    return pares

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

inicio = min(primeiro_numero, segundo_numero)
fim = max(primeiro_numero, segundo_numero)

numeros_pares = encontrar_pares(inicio, fim)

print("Os números pares entre", inicio, "e", fim, "são:", numeros_pares)
