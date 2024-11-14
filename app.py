
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

@app.route('/alunos', methods=['GET', 'POST'])
def professores():
    connection = sqlite3.connect('Cantina_legal.db')
    cursor = connection.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        turma = request.form['']
