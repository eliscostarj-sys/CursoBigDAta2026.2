#CÁLCULO DA MÉDIA ESCOLAR USANDO FOR

for i in range(10):
    print(f"Aluno {i+1} de 10.")

    aluno = str(input("Nome do aluno:"))
    nota_portugues = float(input("Nota de Português:"))
    nota_matematica = float(input("Nota de Matemática:"))
    nota_historia = float(input("Nota de História:"))
    nota_geografia = float(input("Nota de Geiografia:"))

    media_do_aluno = (nota_portugues+nota_matematica+nota_historia+nota_geografia)/4

    print("A média do aluno é: ", media_do_aluno)

    if media_do_aluno > 7:
        print ("Você está aprovado")
    elif media_do_aluno >= 5 and media_do_aluno <= 7:
        print ("Você está em recuperação.")
    else:
        print ("Você está reprovado.")