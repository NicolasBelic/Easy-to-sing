
import mysql.connector as banco
import bcrypt
import requests
 
class usuario: 
    def realiza_login(email,senha):
        sql_select="select email from usuario where email =%s and senha=%s"

        conexao=banco.connect(host="localhost", user="root", password="admin", database="easy_to_sing")

        valores=(email,senha)
        manipulador=conexao.cursor()
        manipulador.execute(sql_select,valores)
        return manipulador.fetchall()

    def insere_login_artista(nome,sexo,telefone,cpf,cep,email,senha,logradouro, bairro, localidade, uf):
        sql_insert="insert into usuario (nome,sexo,telefone,cpf,cep,email,senha,tipo,logradouro, bairro, localidade, uf) values(%s,%s,%s,%s,%s,%s,%s,'artista',%s,%s,%s,%s)"
        cripto = Criptografia()
        senha_hash = cripto.criptografia(senha)
        valores=(nome,sexo,telefone,cpf,cep,email,senha_hash,logradouro, bairro, localidade, uf)


        conexao=banco.connect(host="localhost", user="root", password="admin", database="easy_to_sing")

        cursor=conexao.cursor()
        cursor.execute(sql_insert,valores)
        conexao.commit()


    def insere_login_restaurante(nome,telefone,cnpj,cep,email,senha):
        sql_insert="insert into usuario (nome,telefone,cnpj,cep,email,senha,tipo) values(%s,%s,%s,%s,%s,%s,'restaurante')"
        conexao=banco.connect(host="localhost", user="root", password="admin", database="easy_to_sing")
        cripto = Criptografia()
        senha_hash = cripto.criptografia(senha)
        valores=(nome,telefone,cnpj,cep,email,senha_hash)
        cursor=conexao.cursor()
        cursor.execute(sql_insert,valores)
        conexao.commit()


class Criptografia:
    def criptografia(self, texto):
            salt = bcrypt.gensalt()
            hash_valor = bcrypt.hashpw(texto.encode('utf-8'),salt)
            return hash_valor

class Upload:
    def fotos():
        conexao=banco.connect(host="localhost", user="root", password="admin", database="easy_to_sing")
        with open("image.jpg","rb") as f:
           binary_data = f.read() 

        cursor=conexao.cursor()
        sql_insert="insert into upload (path,data_upload) values(%s,%s)"
        cursor.execute(sql_insert,("nome_da_imagem",binary_data))

        cursor.close()
        conexao.close()

    




