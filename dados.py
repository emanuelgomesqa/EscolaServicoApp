from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return ("Seja Bem vindo ao sistema de gerenciamento dos alunos matriculados, cursos, turmas e as disciplinas existentes no IFPB", 200)

# inicio Recursos da aplicação tb_aluno
@app.route("/alunos", methods=['GET'])
def getAluno():

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return ("Listado com sucesso", 200)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno WHERE id_aluno = ?;
    """, (id,))

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Listado com sucesso", 200)

@app.route("/aluno", methods=['POST'])
def setAluno():

    print ("-------------- Cadastrando Aluno --------------")

    nome = request.form['nome']
    matricula = request.form['matricula']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']

    print(nome, matricula, cpf, nascimento)

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?,?,?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

    return ("Cadastro de Aluno realizado com sucesso!", 200)
# fim Recursos da aplicação tb_aluno
