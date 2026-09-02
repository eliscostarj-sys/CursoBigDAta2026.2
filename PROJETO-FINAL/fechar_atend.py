def fechar_conta(numero_da_mesa, numero_pedido, valor_total):

    print("===== RESUMO DO ATENDIMENTO =====")
    print(f"Mesa número: {numero_da_mesa}")
    print(f"Pedido número: {numero_pedido}")
    print(f"Valor total: R$ {valor_total:.2f}")

    novo_pedido = input("Você deseja acrescentar algo ao seu pedido?" 
                        "\n Digite SIM para continuar ou NÃO para encerrar a conta: ").upper()

if novo_pedido == "SIM":
    return "NOVO_PEDIDO"

elif novo_pedido == "NÃO" or novo_pedido == "NAO":
    print("Finalizando o atendimento...")

    # O sistema verifica o pagamento - VISÃO SIST
    pagamento = input("Pagamento realizado? (S/N): ").upper()

    if pagamento == "S":
            print(f"\nPedido {numero_pedido} ", f"no valor de R$ {valor_total:.2f} foi pago.")
            print(("Conta fechada com sucesso!").upper)

            # Liberação dos recursos do atendimento
            print(f"Mesa {numero_da_mesa} liberada.")
            print("Garçom liberado.")

            #VISÃO CLIENTE
            print(("Obrigada por escolher o Restaurante Tanoshimi!").upper)

            import random
            def gera_cumpom_desc():
                numero = random.randint (1000, 9999)
                

            print("E temos um presentinho para você voltar logo." 
                  "\n Um cupom de R$20,00 de desconto para usar na próxima compra!!!")
            return f"TSHIMI {numero} válido até 30/09/2026."

    print("ATENDIMENTO_FINALIZADO.")

else:
    print(f"Pedido {numero_pedido}", f"no valor de R$ {valor_total:.2f}" 
              "\n está pendente de pagamento.")
    print("A mesa ainda não pode ser liberada." "\n PAGAMENTO_PENDENTE."
          "\n Retorno ao pagamento")
    return registrar_pagamento
