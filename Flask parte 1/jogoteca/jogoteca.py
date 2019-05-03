from flask import Flask, render_template, request, redirect, session, flash, url_for

# Cria instância do Flask
app = Flask(__name__)

# secret_key será usado para encriptar os dados da sessão
app.secret_key = 'alura'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, login, senha):
        self.id = id
        self.login = login
        self.senha = senha
        

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario('lucas', 'lucas', '123')
usuario2 = Usuario('andre', 'andre', '456')
usuario3 = Usuario('joao', 'joao', '789')
usuarios = {usuario1.id : usuario1, usuario2.id : usuario2, usuario3.id : usuario3}


@app.route('/index')
def index():
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

    lista.append(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima_pagina = request.args.get('proxima')
    return render_template('login.html', proxima=proxima_pagina)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if(request.form['usuario'] in usuarios):
        usuario = usuarios[request.form['usuario']]
        if(usuario.senha == request.form['senha']):
            session['usuario_logado'] = usuario.id
            flash('Usuario {} logado com sucesso!'.format(usuario.login))
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


app.run(debug=True)