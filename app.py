from flask import Flask, render_template, request, redirect, g
from tinydb import TinyDB
import sqlite3

app = Flask(__name__)

def ligar_banco():
    banco = g._database = sqlite3.connect('ModaEstilo.db')
    return banco

Db = TinyDB('usuario.json')

@app.route('/autenticar', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    dados = Db.all()

    if dados:
        usuariobanco = dados[0]['Usuario']
        senhabanco = dados[0]['senha']
        if username == usuariobanco and password == senhabanco:
            return render_template('Home.html')
        else:
            return render_template('Login.html', titulo='Home', error=True)


@app.route('/')
def home():
    return render_template('Login.html', titulo='Home')



@app.route('/exibir')
def exibir():
    return render_template('TabelaProdutos.html', titulo="Tabela Produtos", )
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT Produto, Estoque,Preco,Categoria,Tamanho FROM ImagensAPI')
    imagens = cursor.fetchall()
    return render_template('galeria.html', Titulo='Galeria', imagensdb=imagens)

@app.route('/home')
def home_page():
    return render_template('home.html', titulo='Página Inicial')



@app.route('/produtos')
def lista_produtos():
    produtos = [...]
    produtos_por_pagina = 12
    pagina_atual = int(request.args.get('pagina', 1))
    inicio = (pagina_atual - 1) * produtos_por_pagina
    fim = inicio + produtos_por_pagina
    produtos_paginados = produtos[inicio:fim]
    total_paginas = (len(produtos) + produtos_por_pagina - 1) // produtos_por_pagina

    return render_template('TabelaProdutos.html', produtos=produtos_paginados,
                           pagina_atual=pagina_atual, total_paginas=total_paginas)

@app.route('/vendas')
def ListarVendas():
    return render_template('Ta', )

@app.route('/editarProdutos')
def editar_produtos():
    return render_template('editarP.html', titulo='Editar Produtos')


@app.route('/editarVendas')
def editar_vedas():
    return render_template('editarV.html', titulo='Editar Produtos')



@app.route('/cadastrarProdutos')
def cadastar_produtos():
    return render_template('CadastroP.html', titulo='Cadastro')


@app.route('/criar', methods=['POST'])
def criar_produto():
    produto = request.form['produto']
    estoque = request.form['estoque']
    preco = request.form['preco']
    categoria = request.form['categoria']
    tamanho = request.form['tamanho']
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('INSERT INTO Produtos(Produto, Estoque, Preco, Categoria,Tamanho)'
                   'VALUES (?,?,?,?,?);', (produto, estoque,preco,categoria,tamanho))
    banco.commit()
    return redirect('/cadastrarProdutos')







if __name__ == '__main__':
    app.run()
