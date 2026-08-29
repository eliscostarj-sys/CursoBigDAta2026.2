#FUNÇÕES E MÓDULOS

#SORTEIO DE NÚMEROS

import random

numero_random = random.randint(1,30) #sorteio aleatório de números

print(numero_random)

def sorteiame():
    #aspas tripla são usadas para comentar o objetivo de uma função /clasee.
    ''' 
    Algoritmo escolhe e retorna um números 
    inteiro aleaatório no intervalo de 1 a 30.
    ''' 
    numero_random = random.randint(1,30)

    return numero_random #return tem função similar ao print: ele pede para mostrar algo; só pode ser usado em funções

resultado = sorteiame()
print(resultado)

