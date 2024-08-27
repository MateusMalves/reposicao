import main

def exibir_menu():
    print("\nCalculadora")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def realizar_operacao(operacao):
    if operacao in [1, 2, 3, 4]:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    
    if operacao == 1:
        resultado = main.soma(a, b)
        print("Resultado: ", resultado)
    elif operacao == 2:
        resultado = main.subtracao(a, b)
        print("Resultado: ", resultado)
    elif operacao == 3:
        resultado = main.multiplicacao(a, b)
        print("Resultado: ", resultado)
    elif operacao == 4:
        resultado = main.divisao(a, b)
        print("Resultado: ", resultado)
    elif operacao == 5:
        print("Saindo...")
    else:
        print("Opção inválida!")

def main_loop():
    while True:
        exibir_menu()
        try:
            operacao = int(input("Escolha uma operação: "))
            if operacao == 5:
                realizar_operacao(operacao)
                break
            elif operacao in [1, 2, 3, 4]:
                realizar_operacao(operacao)
            else:
                print("Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

if __name__ == "__main__":
    main_loop()
