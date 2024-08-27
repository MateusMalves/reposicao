import math

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_perimetro_quadrado(lado):
    return 4 * lado

def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_perimetro_retangulo(comprimento, largura):
    return 2 * (comprimento + largura)

def calcular_area_circulo(raio):
    return math.pi * raio * raio

def calcular_perimetro_circulo(raio):
    return 2 * math.pi * raio

# Exemplo de uso
forma = input("Digite a forma geométrica (quadrado, retangulo, circulo): ")

if forma == "quadrado":
    lado = float(input("Digite o lado do quadrado: "))
    area = calcular_area_quadrado(lado)
    perimetro = calcular_perimetro_quadrado(lado)
    print(f"A área do quadrado é: {area}")
    print(f"O perímetro do quadrado é: {perimetro}")
elif forma == "retangulo":
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    area = calcular_area_retangulo(comprimento, largura)
    perimetro = calcular_perimetro_retangulo(comprimento, largura)
    print(f"A área do retângulo é: {area}")
    print(f"O perímetro do retângulo é: {perimetro}")
elif forma == "circulo":
    raio = float(input("Digite o raio do círculo: "))
    area = calcular_area_circulo(raio)
    perimetro = calcular_perimetro_circulo(raio)
    print(f"A área do círculo é: {area}")
    print(f"O perímetro do círculo é: {perimetro}")
else:
    print("Forma geométrica inválida.")