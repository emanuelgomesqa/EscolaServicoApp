from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return ("Seja Bem vindo ao sistema de gerenciamento dos alunos matriculados, cursos, turmas e as disciplinas existentes no IFPB", 200)

# inicio Recursos da aplicação tb_escola

@app.route("/escolas", methods=['GET'])
def getEscola():
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_escola;
    """)

    for linha in cursor.fetchall():
        return(linha)

    conn.close()

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):
    pass

@app.route("/escola", methods=['POST'])
def CadastroEscola():

    print ("-------------- Cadastrando Escola --------------")

    nome = request.form['nome']
    logradouro = request.form['logradouro']
    cidade = request.form['cidade']

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?,?,?);
    """, (nome,logradouro, cidade))

    conn.commit()
    conn.close()

    return ("Cadastro de Escola realizado com sucesso!", 200)

# fim Recursos da aplicação tb_escola


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
