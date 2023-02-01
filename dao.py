
import mysql.connector as banco

def realiza_login(email,senha):
    sql_select="select email from usuario where email =%s and senha=%s"

    conexao=banco.connect(host="localhost", user="root", password="adim", database="easy_to_sing")

    valores=(email,senha)
    manipulador=conexao.cursor()
    manipulador.execute(sql_select,valores)
    return manipulador.fetchall()

def insere_login_artista(nome,sexo,telefone,cpf,cep,email,senha,logradouro, bairro, localidade, uf):

    

    sql_insert="insert into usuario (nome,sexo,telefone,cpf,cep,email,senha,tipo,logradouro, bairro, localidade, uf) values(%s,%s,%s,%s,%s,%s,%s,'artista',%s,%s,%s,%s)"
    

    conexao=banco.connect(host="localhost", user="root", password="adim", database="easy_to_sing")

    valores=(nome,sexo,telefone,cpf,cep,email,senha,logradouro, bairro, localidade, uf)
    cursor=conexao.cursor()
    cursor.execute(sql_insert,valores,)
    conexao.commit()

def insere_login_restaurante(nome,telefone,cnpj,cep,email,senha):


    sql_insert="insert into usuario (nome,telefone,cnpj,cep,email,senha,tipo) values(%s,%s,%s,%s,%s,%s,'restaurante')"
    conexao=banco.connect(host="localhost", user="root", password="adim", database="easy_to_sing")

    valores=(nome,telefone,cnpj,cep,email,senha)
    cursor=conexao.cursor()
    cursor.execute(sql_insert,valores,)
    conexao.commit()