# 1. Definindo uma função simples
def saudacao():
    print("Olá, mundo!")


# 2. Função com parâmetros e retorno
def somar(a, b):
    return a + b
a= float(input("Digite o primeiro número: "))
b= float(input("Digite o segundo número: "))

print(f"A soma de {a} e {b} é: {somar(a, b)}")



# 3. Função lambda
dobro = lambda x: x * 2

# 4. Usando *args e **kwargs
def somar_tudo(*args):
    return sum(args)

def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


# 5. Função com return e yield
def gerar_numeros():
    for i in range(5):
        yield i

def multiplicar(a, b):
    return a * b
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(f"O resultado da multiplicação é: {multiplicar(a, b)}")


# 6. Funções como objetos de primeira classe
def cumprimentar():
    return "Olá"

def executar_funcao(func):
    return func()

quadrado = lambda x: x ** 2

# 7. Usando map() e filter()
numeros = [1, 2, 3, 4, 5]
dobros = list(map(lambda x: x * 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))


# Demonstração no terminal
if __name__ == "__main__":
    # Saudação simples
    saudacao()

    # Soma simples com parâmetros
    resultado_soma = somar(10, 20)
    print(f"Soma de 10 e 20: {resultado_soma}")

    # Usando a função lambda para dobrar
    print(f"O dobro de 5 é: {dobro(5)}")

    # Somando tudo com *args
    resultado = 0
    resultado_somar_tudo = somar_tudo(1, 2, 3, 4)
    print(f"Soma total de 1, 2, 3, 4: {resultado_somar_tudo}")

    # Exibindo informações com **kwargs
    exibir_info(nome="Mateus", idade=27, cidade="Tóquio")

    # Usando yield para gerar números
    for numero in gerar_numeros():
        print(f"Gerado: {numero}")

    # Multiplicação simples
    resultado_multiplicacao = multiplicar(5, 6)
    print(f"Multiplicação de 5 e 6: {resultado_multiplicacao}")

    # Funções como objetos de primeira classe
    mensagem = executar_funcao(cumprimentar)
    print(mensagem)

    # Usando map() para dobrar números
    print(f"Números dobrados: {dobros}")

    # Usando filter() para filtrar números pares
    print(f"Números pares: {pares}")
