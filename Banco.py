import sqlite3
conexao = sqlite3.connect('ModaEstilo.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Produtos '
               '(ID INTEGER PRIMARY KEY, '
               'Produto TEXT, '
               'Estoque INTEGER,'       
               ' Preco REAL,'
               'Categoria TEXT,'
               'Tamanho TEXT)'

)