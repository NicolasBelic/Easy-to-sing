
import mysql.connector as banco


import bcrypt


class usuario: 

    def realiza_login(email, senha):
        sql_select = "SELECT id FROM artistas WHERE email = %s AND senha = %s"
        connection = banco.connect(
            host="localhost", 
            user="root", 
            password="adim", 
            database="easy_to_sing"
        )
        cursor = connection.cursor()
        cursor.execute(sql_select, (email, senha))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def insere_artista(nome, sexo, telefone, cpf, cep, email, senha, logradouro, bairro, localidade, uf):
        sql_insert = "INSERT INTO artistas (nome, sexo, telefone, cpf, cep, email, senha, logradouro, bairro, localidade, uf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        connection = banco.connect(
            host="localhost", 
            user="root", 
            password="adim", 
            database="easy_to_sing"
        )
        cripto = Criptografia()
        senha_hash = cripto.criptografia(senha)
        cursor = connection.cursor()
        cursor.execute(sql_insert, (nome, sexo, telefone, cpf, cep, email, senha_hash, logradouro, bairro, localidade, uf))
        connection.commit()
        cursor.close()
        connection.close()



    def insere_empreendimento(nome,telefone,cnpj,cep,email,senha,logradouro,bairro,localidade,uf):
        sql_insert = "INSERT INTO empreendimentos (nome, telefone, cnpj, cep, email, senha, tipo, logradouro, bairro, localidade, uf) VALUES (%s, %s, %s, %s, %s, %s, 'restaurante', %s, %s, %s, %s)"
        conexao = banco.connect(host="localhost", user="root", password="adim", database="easy_to_sing")
        cripto = Criptografia()
        senha_hash = cripto.criptografia(senha)
        valores = (nome, telefone, cnpj, cep, email, senha_hash, logradouro, bairro, localidade, uf)
        cursor = conexao.cursor()
        cursor.execute(sql_insert, valores)
        conexao.commit()



class Criptografia:
    def criptografia(self, texto):
            salt = bcrypt.gensalt()
            hash_valor = bcrypt.hashpw(texto.encode('utf-8'),salt)
            return hash_valor

class Upload:
    def fotos(self):
        conexao=banco.connect(host="localhost", user="root", password="adim", database="easy_to_sing")
        with open("image.jpg","rb") as f:
           binary_data = f.read() 

        cursor=conexao.cursor()
        sql_insert="insert into upload (path,data_upload) values(%s,%s)"
        cursor.execute(sql_insert,("nome_da_imagem",binary_data))

        cursor.close()
        conexao.close()
