from flask import Flask, request
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
        print(linha)

    conn.close()

    return ("Listado com sucesso", 200)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_escola WHERE id_escola = ?;
    """, (id,))

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Listado com sucesso", 200)

@app.route("/escola", methods=['POST'])
def setEscola():

    print ("-------------- Cadastrando Escola --------------")

    nome = request.form['nome']
    logradouro = request.form['logradouro']
    cidade = request.form['cidade']

    print(nome, logradouro, cidade)

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

# inicio Recursos da aplicação tb_aluno
# fim Recursos da aplicação tb_aluno


# inicio Recursos da aplicação tb_escola
# fim Recursos da aplicação tb_escola


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
