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
    dados=dao.realiza_login(email,senha)


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

    dao.insere_login_artista(nome,sexo,telefone,cpf,cep,email,senha) 
    return render_template('easy_to_sing.html')

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

    dao.insere_login_restaurante(nome,telefone,cnpj,cep,email,senha) 
    return render_template('easy_to_sing.html')            

@app.route('/Perfil')
def abre_perfil():
    return render_template('perfil.html')

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
    app.run(debug=True)