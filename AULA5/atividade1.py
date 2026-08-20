#Cálculo de Lâmpadas

POTENCIA = 3    #Potência da lâmpada
largura = float(input("Informe a largura do cômodo:"))
comprimento = int(input("Informe o comprimento do cômodo:"))
calculo = ((largura*comprimento)/POTENCIA)

resposta = (f"Você precisa de {calculo} lâmpadas")

print(resposta)
