#Cálculo de caixas de azulejos para cozinha retangular

CX_AZULEJO = 1.5
comprimento = float(input("Informe o comprimento da cozinha:"))
largura = float(input("informe a largura da cozinha:"))
altura = float(input("Informe a altura da parede:"))

calculo = ((comprimento*largura*altura)/CX_AZULEJO)

quant_caixas = (f"Você precisa de {calculo} caixas de azulejo.")

print(quant_caixas)