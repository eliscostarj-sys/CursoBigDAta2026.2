
# impar_1 = 3
# impar_2 = 5
# impar_3 = 13
# impar_4 = 27

# impares = [] #criação de uma lista de números impar ao invés de várias entradas, como acima; cochetes está associado à lista.
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[0]) # vou tupxar o número da lista que está na posição "0". Também é possivel solicitar na ordem inversa, inserindo o sinal de -
# print(impares[-2])

# lista_01 =[
#     12,
#     "Pedro",
#     12.53343,
#     "[{_{^^{}}}",
#     False,
#     0,
#     [2,4,6,8]
# ] #é possível quebrar os ites da lista em linhas

# print(lista_01[1],lista_01[2],lista_01[6][2])

# #CONDICIONAIS
# lista_02 = ["Márcia"]
# if "Márcia" in lista_02:
#     print(lista_02) #verifica se algo está contido ou não em um conjunto.
# else:
#     print("Márcia não está presente na lista")

# #LOOPINGS:

participantes = ["Isaque","Luana","Maria"]

# for participantes in participantes:
#     print(participantes)

partic_2 = "Hugo"
participantes.append(partic_2) #acrescenta o item no fim da lista
participantes.insert(2,partic_2) # tem que definir os parâmetro "onde" e "quem"
participantes.pop(1) #remove os índices
participantes.remove("Hugo") #removeu a pimeira ocorrencia / pilha e fila
participantes.reverse() #inverte a ordem dos índices na list
participantes.count("Hugo") # verifica qual é a ordem do indice na lista
participantes.index("Maria")
participantes.clear() #limpa todo o conteúdo da lista



print(participantes)


#SETS
# numeros_pares = { # O SET não guarda a ordem, portanto, o que foi digitado dentro dele mudará a ordem quando imprimo, tb removeu / não permite as duplicações; PARA TRABALHAR COM EMBARALHAMENTO DOS DADOS.
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292, 
#     202
# }
# #print(numeros_pares, type(numeros_pares)) 

# #COMANDOS
# numeros_impares = {111, 111, 112, 291, 291, 205}
# print(numeros_pares.intersection(numeros_impares))

# numeros_pares.remove(205)
# print(numeros_pares)

#DICIONÁRIOS:

produtos = {"maçã": 5.99, "laranja": 4.79} #Chave-valor; é possível ter uma chave sem valor, mas não o oposto.
print(produtos,(type(produtos)))
print(produtos.items())
print(produtos.keys)
print(produtos.values())
print(produtos.get("laranja")) #lembro a chave, mas não o valor
produtos2 = produtos.copy() #criei uma cópia/clone do arquivo/entrada original - boas práticas: nunca mudar no original; torna-se possível posterior comparação entre o original e a cópia.
print(produtos2)
produtos2.pop("maçã")
produtos2["maçã:"]=7.99
print(produtos2)

achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)



