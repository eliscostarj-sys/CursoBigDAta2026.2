import pandas as pd

df=pd.read_csv('vendas_produtos.csv')
print(df.head())

import mysql.connector

#conectar banco de dados
conexao = mysql.connector.connect(
    host = "localhost"
    user = "root"
    pasword = ""
    data_base = "vendas_online2"
)

# 2. Criar um objeto cursor para executar as queries
cursor = conexao.cursor()

# 3. Definir o query
query = "SELECT * FROM produtos"

# 4. Executar o query
cursor.execute(query)

# 5. Obter os resultados
resultados = cursor.fetchall()

# 6. Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão
cursor.close()
conexao.close()
