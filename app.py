
from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3 

app = Flask(__name__)

def init_db ():
    connection = sqlite3.connect ('Cantina_legal.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            turma INTEGER,
            email TEXT,
            senha INTEGER
        )
    ''')
    connection.commit()
    connection.close()

@app.route('/Cantina_legal', methods=['GET', 'POST'])
def alunos():
    connection = sqlite3.connect('Cantina_legal.db')
    cursor = connection.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        turma = request.form['turma']
        email = request.form['email']
        senha = request.form['senha']

        cursor.execute("INNSERT INTO alunos (nome, turma, email, senha) VALUES (?, ?, ?, ?)", (nome, turma, email, senha))
        connection.commit()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        connection.close()

    html_code = '''
    <DOCTYPE html>
    <html lang= "pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device width, initial-scale
        <title>Cantina_legal</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            table { width: 50%; margin: auto; border-collapse: collapse; }
            th, td { padding: 8px 12px; border: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            form { margin: 20px auto; width: 300px; text-align: left; }
            input[type="text"] { width: 100%; padding: 8px; margin: 5px 0; }
            input[type="submit"] { padding: 8px 12px; background-color: #4CAF50; color: white;
border: none; }
        </style>
    </head>from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3 

app = Flask(__name__)

def init_db ():
    connection = sqlite3.connect ('Cantina_legal.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            turma INTEGER,
            email TEXT,
            senha INTEGER
        )
    ''')
    connection.commit()
    connection.close()

@app.route('/alunos', methods=['GET', 'POST'])
def professores():
    connection = sqlite3.connect('Cantina_legal.db')
    cursor = connection.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        turma = request.form['']

    <body>
        <h2>Formulário: Adicionar aluno</h2>

        <form method="POST">
            <label for="nome">Nome:</label><br>
            <input type="text" id="nome" name="nome" required><br>
            <label for="turma">turma:</label><br>
            <input type="text" id="turma" name="turma" required><br><br>
            <input type="submit" value="Adicionar aluno">
        </form>
        <h2>Lista de alunos</h2>
    </body>
    </html>
    '''
    return render_template_string(html_code, )
if __name__ == '__main__':
    init_db() 
    app.run(debug=True)
