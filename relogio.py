def saudacao(horario):
    if horario >= 0 and horario < 12:
        print("Bom dia!")
    elif horario >= 12 and horario < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

# Exemplo de uso da função
saudacao(9)  # Imprime "Bom dia!"
saudacao(15)  # Imprime "Boa tarde!"
saudacao(20)  # Imprime "Boa noite!"

