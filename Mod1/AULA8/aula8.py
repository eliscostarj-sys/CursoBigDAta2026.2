<<<<<<< HEAD

def calculadora_v1(num1,num2,operador): #definindo uma função
# num1=float(input("Digite seu primeiro número"))
# num2=float(input("Digite seu primeiro número"))

operador=input("Informe a operação desejada entre: 1. adição 2. subtração 3. multiplicação e 4. divisão")

# match operador:
#     case "1":
#         print(f"Resultado da soma: {num1+num2}.")
#     case "2":
#         print(f"Resultado da subtração: {num1-num2}.")
#     case "3":
#         print(f"Resultado da multiplicação {num1*num2}.")
#     case "4":
#         if num2!=0:
#             print(f"Resultado da divisão: {num1/num2}.")
#         else:
#             print(f"Dividiu por zero. Errou feio")
#     case _ :
#         print("Informe um número de operador válido.")

# calculo = calculadora_v1(333,555,operador=1) #chamando uma função

match operador:
    case "1":
        resultado = (num1+num2)
    case "2":
       rsultado = (num1-num2)
    case "3":
      resultado = (num1*num2)
    case "4":
        if num2!=0:
            resultado = num1/num2
            print(f"Resultado da divisão: {num1/num2}.")
        else:
            print(f"Dividiu por zero. Errou feio")
    case _ :
        print("Informe um número de operador válido.")

     return(calculo)

calculo = calculadora_v1(333,555,operador=1) #chamando uma função



=======

def calculadora_v1(num1,num2,operador): #definindo uma função
# num1=float(input("Digite seu primeiro número"))
# num2=float(input("Digite seu primeiro número"))

operador=input("Informe a operação desejada entre: 1. adição 2. subtração 3. multiplicação e 4. divisão")

# match operador:
#     case "1":
#         print(f"Resultado da soma: {num1+num2}.")
#     case "2":
#         print(f"Resultado da subtração: {num1-num2}.")
#     case "3":
#         print(f"Resultado da multiplicação {num1*num2}.")
#     case "4":
#         if num2!=0:
#             print(f"Resultado da divisão: {num1/num2}.")
#         else:
#             print(f"Dividiu por zero. Errou feio")
#     case _ :
#         print("Informe um número de operador válido.")

# calculo = calculadora_v1(333,555,operador=1) #chamando uma função

match operador:
    case "1":
        resultado = (num1+num2)
    case "2":
       rsultado = (num1-num2)
    case "3":
      resultado = (num1*num2)
    case "4":
        if num2!=0:
            resultado = num1/num2
            print(f"Resultado da divisão: {num1/num2}.")
        else:
            print(f"Dividiu por zero. Errou feio")
    case _ :
        print("Informe um número de operador válido.")

     return(calculo)

calculo = calculadora_v1(333,555,operador=1) #chamando uma função



>>>>>>> 35b78381c411afd39936138d64be4a4633a825d5
