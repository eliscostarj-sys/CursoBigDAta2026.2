# Desafio 2, aula 2: Cálculo de média e status do estudante.

nota_portugues = 7.5
nota_matematica = 8.7
nota_historia = 6.1
nota_geografia = 3.8

media_do_aluno = (nota_portugues+nota_matematica+nota_historia+nota_geografia)/4

print("A média do aluno é: ", media_do_aluno)

if media_do_aluno > 7:
    print ("Você está aprovado")
elif media_do_aluno >= 5 and media_do_aluno <= 7:
    print ("Você está em recuperação.")
else:
    print ("Você está reprovado.")




