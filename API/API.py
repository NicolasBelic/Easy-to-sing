import requests

cep = input("Qual seu Cep ?")

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

if response.status_code == 200:
    data = response.json()
    n1 =data['logradouro'], data['bairro'], data['localidade'], data['uf']
    print(n1)
else:
    print(f'Erro ao obter dados para o CEP {cep}')
