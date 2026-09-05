#Rendimento do taxista
PRECO_COMBUSTIVEL = 6.15
km_inicio = float(input("Informe o Km inicial do dia de trabalho:"))
km_fim = float(input("Informe o km do final do dia de trabalho:"))
quant_combustivel = float(input("Informe quantos litros de combustível você usou:"))
valor_recebido = float(input("Informe o valor total recebido hoje:"))

valor_pago_combustivel = (quant_combustivel*PRECO_COMBUSTIVEL)
media_consumo =((km_fim - km_inicio)/quant_combustivel)
lucro_liquido =(valor_recebido-valor_pago_combustivel)

print("A média de consumo de hoje é de:", media_consumo)
print("O seu lucro líquido de hoje é de R$",lucro_liquido)