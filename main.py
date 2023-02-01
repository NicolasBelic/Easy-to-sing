from flask import Flask, render_template,request,redirect,url_for
import dao


app =Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def realiza_login():
    email=request.form['email']
    senha=request.form['senha']
<<<<<<< HEAD
    dados=dao.realiza_login(email,senha)
=======
    dados=dao.usuario.realiza_login(email,senha)
>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f


    if len(dados)>0:
        return render_template("easy_to_sing.html")    
    else:
        return render_template("login.html") 

 
@app.route('/entra_criar_conta')
def criar_conta():
    return render_template('criar_conta.html')

@app.route('/cadastro_artista')
def abre_cadastro_artista():
    return render_template('cadastro_artista.html')    

@app.route('/cadastrar_artista', methods=['POST'])
def salva_login_artista():
    nome=request.form['nome']
    sexo=request.form['sexo']
    telefone=request.form['telefone']
    cpf=request.form['cpf']
    cep=request.form['cep']
    email=request.form['email']
    senha=request.form['senha']

<<<<<<< HEAD
    
=======
>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f
    import requests

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    data = response.json()
    logradouro = data['logradouro']
    bairro = data['bairro']
    localidade = data['localidade']
    uf = data['uf']

<<<<<<< HEAD
    dao.insere_login_artista(nome, sexo, telefone, cpf, cep, email, senha, logradouro, bairro, localidade, uf) 
    return render_template('easy_to_sing.html')

=======
    dao.usuario.insere_login_artista(nome, sexo, telefone, cpf, cep, email, senha, logradouro, bairro, localidade, uf) 
    return render_template('easy_to_sing.html')


>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f
@app.route('/cadastro_restaurante')
def abre_cadastro_restaurante():
    return render_template('cadastro_restaurante.html')

@app.route('/cadastrar_restaurante', methods=['POST'])
def salva_login_restaurante():
    nome=request.form['nome']
    telefone=request.form['telefone']
    cnpj=request.form['cnpj']
    cep=request.form['cep']
    email=request.form['email']
    senha=request.form['senha']

<<<<<<< HEAD
    dao.insere_login_restaurante(nome,telefone,cnpj,cep,email,senha) 
=======
    dao.usuario.insere_login_restaurante(nome,telefone,cnpj,cep,email,senha) 
>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f
    return render_template('easy_to_sing.html')            

@app.route('/Perfil')
def abre_perfil():
<<<<<<< HEAD
    return render_template('perfil.html')
=======
    return render_template('meuperfil.html')

@app.route("/postar_foto", methods=['POST'])
def postar_foto_perfil():
    arquivo=request.form['arquivo']

    dao.Upload.fotos(arquivo())
    return render_template('meuperfil.html')    

>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f

@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route("/home")
def home():
    return render_template('easy_to_sing.html')

@app.route("/Chat")
def abre_chat():
    return render_template('chat.html')

@app.route("/abre_chat")
def chat_de_conversa():
    return render_template('chat.html')

@app.route("/iniciar_conversa")
def iniciar_conversa_feed():
    return render_template('chat.html')    


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> b57b6ef421dc076890bb31c4c833ad400604460f
