#CÓD DE ORIGEM DO PRODUTO

cod_origem = int(input("Digite o código do produto:"))

match cod_origem:
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5:
        print("Nordeste")  
    case 6:
        print("Nordeste")
    case 7:
        print("Sudeste")
    case 8:
        print("Sudeste")
    case 9:
        print("Sudeste")
    case 10:
        print("Centro-Oeste")
    case 11:
        print("Noroeste")
    case _:
        print("Produto Importado")
    
