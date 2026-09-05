# Média do aluno com optativa

Nota1 = float(input("Digite a nota da matéria 1:"))
Nota2 = float(input("Digite a nota da matéria 2:"))
Nota_optativa = float(input("Digite a nota da matéria optativa:")) #a nota será registrada como -1 quando o aluno não tiver feito matéria optativa

if Nota1 < Nota2 and Nota_optativa > Nota1:
    Nota1 = Nota_optativa
elif Nota2 < Nota1 and Nota_optativa > Nota2:
    Nota2 = Nota_optativa

media = (Nota1 + Nota2) / 2
print(f"Sua média é:{media}")

if media >= 6:
    print("Aprovado")

elif media >= 3 and media <6:
    print("Recuperação")

else: 
    print("Reprovado")
