print("Olá, mundo!")

nome = "Maria"      #str: texto, isto
idade = 30           #int: número inteiro
preco = 19.99       #floot: números com casas decimais
esta_matricula = True   #boll: booleano - valor lógico True False
notas = [8.0, 7.5]      #list: coleção ordenada
aluno = ("Maria", 30)   #tuple: coleção ordenadas
disciplinas = {"Python", "Lógica"}  #set: conjunto
cadastros = {"nome": "Maria", "idade": 30} #dict: 

# a função type () permite consultar o tipo de comando
print(type(nome))
print(type(idade))
print(type(preco))

x = 15
y = 20
print("x é maior que y?", x > y)
print("x é igual a y?", x == y)
resposta = x>y
print(resposta)
print(type(resposta))

tem_carteira = True
idade = 18
tem_carro = False
pode_dirigir = idade >= 18 

print("Pode dirigir?")


cnh = True
bebidinha =  False

posso_dirigir = cnh and  not bebidinha
print(posso_dirigir)

#2o ex de condicionais
onibus = True
trem = True

venho_pra_aula = onibus or trem
print("venho pra aula?", venho_pra_aula)

# 3 EX
locomocao = "moto"  #definição da variável 1
choveu = True       #definição da variável 2

if choveu and locomocao == "moto": 
    resultado = "socorro"   #identação
elif not choveu and locomocao == "moto":
else:
    resultado = "ótimo"

print(resultado)


     