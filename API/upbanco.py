import mysql.connector
import requests
import cep

# Faz uma requisição para a API e obtém os dados do endereço
cep = cep.cep
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
dados_endereco = response.json()

# Armazena os dados do endereço em variáveis
cep = dados_endereco['cep']
logradouro = dados_endereco['logradouro']
bairro = dados_endereco['bairro']
localidade = dados_endereco['localidade']
uf = dados_endereco['uf']

# Conecta ao banco de dados MySQL
cnx = mysql.connector.connect(user='root', password='adim', host='localhost', database='enderecos')
cursor = cnx.cursor()

# Insere os dados do endereço em uma tabela no banco de dados
query = f'INSERT INTO enderecos (cep, logradouro, bairro, localidade, uf) VALUES ("{cep}", "{logradouro}", "{bairro}", "{localidade}", "{uf}")'
cursor.execute(query)

# Salva as mudanças no banco de dados
cnx.commit()

# Fecha a conexão com o banco de dados
cursor.close()
cnx.close()

