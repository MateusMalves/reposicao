num_alunos = int(input("Digite o número de alunos: "))

for i in range(num_alunos):
    nome_aluno = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print(f"O aluno {nome_aluno} foi aprovado!")
    else:
        print(f"O aluno {nome_aluno} foi reprovado.")