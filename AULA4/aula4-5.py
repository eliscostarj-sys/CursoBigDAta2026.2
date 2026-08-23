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

for i in range (-10):
    print (i)

for i in range(1,10,2):
    print (i)
    
for i in range(1,102,-2):
    print (i)

#while
somador = int(input("Registro:"))
controle = 0

while controle <= 30:   #quando ultrapassa essa consição, ele não lê os comandos abaixo identados.
    controle=controle+somador
    somador = int(input("Registro:"))

print("Oficina Lotada!")

#FOR
for i in range(5):
    try:
        print(f"Número {1 + 1} de 5:")
        num = float(input("Digite um número:"))

        dobro = num * 2
        triplo = num * 3
        quadruplo = num * 4

        print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quadruplo={quadruplo}/n") 

    except ValueError:
        print("Entrada Inválida. Tente novamente.")
        num = float(input("Digite um número: "))

acertou = 0
while acertou<5:
    print(f"Número{acertou+1} de 5.")
    num = float(input("Digite um número:"))

    drobro=num*2
    triplo=num*3
    quadruplo=num*4

    print(f"Resultado: Dobro={dobro}, Triplo={triplo}, Quadruplo={quadruplo}\n")
    acertou+=1

    
# DO WHILE

contador = 0
limite = 5

while True
    if contador >= limite:
        break

    try:
        print(f"Número {contador} + 1 de {limite}:")
        



