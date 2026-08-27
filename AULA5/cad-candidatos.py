#CADASTRO DE CANDIDATOS

for i in range(12):
    print(f"cadastro {i+1} de 12")

    ano_nascimento = int(input("Informe o ano do seu nascimento:"))
    ano_atual = 2026
    idade = (ano_atual-ano_nascimento)
    
    if idade<18:
        print("Não é possível realizar o seu cadastro, pois você tem menos de 18 anos.")
        continue

    elif idade>=18:
        nome = input("Nome:")
        email = input("E-mail:")
        telefone = int(input("Telefone:"))
        endereco = input("Endereço:")

        print("Cadastro realizado com sucesso!")

