# Desafio 11, aula 2: Ordenação de 3 números

num1 = 610
num2 = 45
num3 = 12

print("Números em ordem crescente: ")

if num1 <= num2 <= num3:
    print(num1, num2, num3)
elif num1 <= num3 <= num2:
    print (num1, num3, num2)
elif num2 <= num1 <= num3:
    print(num2, num1, num3)
elif num2 <=num3 <= num1:
    print (num2, num3, num1)
elif num3<= num1 <= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)


