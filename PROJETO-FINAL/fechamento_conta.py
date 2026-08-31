# FECHAMENTO DA CONTA
numero_mesa = input("Informe o número da mesa: ")
numero_pedido = input("Digite o número do pedido: ")
valor_consumido = float(input("Digite o valor consumido: R$ "))
pagamento = input("A conta foi paga? (S/N): ")

if pagamento == "S":
    print(f"Pedido {numero_pedido} no valor de R$ {valor_consumido:.2f} foi pago.")
    print("Conta fechada com sucesso!")
    print(f"Mesa {numero_mesa} liberada.")
else:
    print(f"Pedido {numero_pedido} no valor de R$ {valor_consumido: 2f}está pendente de pagamento.")
