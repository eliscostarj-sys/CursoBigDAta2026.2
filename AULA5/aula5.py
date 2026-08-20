#exemplo 1 de condicional sem o match/case
nome = input("Informe seu nome:")

if nome=="Pyetro":
    resposta="Pyetro presente!"
elif nome=="Phellipe":
    resposta="Phellipe presente!"
elif nome=="Elis":
    resposta="Elisangela presente!"


    #exemplo2 com o condicionais if if else

mes = int(input("Informe o mês do seu nascimento:"))

if mes==1:
    signo="Capricornio"
elif mes==2:
    signo="Peixes"
elif mes==3:
    signo="Aquário"
elif mes==4:
    signo="Gêmeos"
elif mes==5:
    signo="Sagitário"
elif mes==6:
    signo="Libra"
elif mes==7:
    signo="Escorpião"
elif mes==8:
    signo="Touro"
elif mes==9:
    signo="Aries"
elif mes==10:
    signo="Virgem"
elif mes==11:
    signo="Leão"
else:
    signo="Isso é trote"

print(f"seu signo é {signo}.")

#exemplo 4 com match case

match mes:
    case 1:
        signo="Aquário"
    case 2:
        signo="Aries"
    case 3:
        signo="Touro"
    case 4:
        signo="Gêmeos"
    case 5:
        signo="Câncer"
    case _:
        signo="Número do mês inválido"

print(f"{signo}.")

meunome = "Elis"

for i in meunome:
    print(i)









#exemplo 3 com match case
