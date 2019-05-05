from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_mysqldb import MySQL
from models import Jogo, Usuario
from dao import JogoDao, UsuarioDao
import os
import time

# Cria instância do Flask
app = Flask(__name__)

# secret_key será usado para encriptar os dados da sessão
app.secret_key = 'alura'

app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
db = MySQL(app)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html',titulo='Novo jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()

    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    #lista.append(jogo)

    return redirect(url_for('index'))


@app.route('/edita/<int:id>')
def edita(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('edita')))

    jogo = jogo_dao.busca_por_id(id)

    nome_imagem = recupera_imagem(id)

    return render_template('edita.html',titulo='Edita jogo', jogo=jogo, capa_jogo=nome_imagem)


@app.route('/atualiza', methods=['POST'])
def atualiza():
    id = request.form['id']
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console, id)

    jogo_dao.salvar(jogo)
    # lista.append(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']

    timestamp = time.time()

    deleta_imagem(jogo.id)

    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/remove/<int:id>')
def remove(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('index')))

    flash("O jogo foi removido com sucesso!")
    jogo_dao.deletar(id)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima')
    return render_template('login.html', proxima=proxima_pagina)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario_existe = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario_existe:
        if(usuario_existe.senha == request.form['senha']):
            session['usuario_logado'] = usuario_existe.id
            flash('Usuario {} logado com sucesso!'.format(usuario_existe.login))
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario ou senha inválidos! Tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo


def deleta_imagem(id):
    imagem = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], imagem))


app.run(debug=True)