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
        VALUES(?,?,?,?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

    return ("Cadastro de Aluno realizado com sucesso!", 200)

# inicio Recursos da aplicação tb_aluno

# inicio Recursos da aplicação tb_curso

@app.route("/cursos", methods=['GET'])
def getCurso():

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return ("Listado com sucesso", 200)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso WHERE id_curso = ?;
    """, (id,))

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Listado com sucesso", 200)

@app.route("/curso", methods=['POST'])
def setCurso():

    print ("-------------- Cadastrando Curso --------------")

    nome = request.form['nome']
    turno = request.form['turno']

    print(nome, turno)

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?,?);
    """, (nome, turno))

    conn.commit()
    conn.close()

    return ("Cadastro de Curso realizado com sucesso!", 200)
# fim Recursos da aplicação tb_curso

# inicio Recursos da aplicação tb_turma

@app.route("/turmas", methods=['GET'])
def getTurmas():

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return ("Listado com sucesso", 200)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma WHERE id_turma = ?;
    """, (id,))

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Listado com sucesso", 200)

@app.route("/turma", methods=['POST'])
def setTurma():

    print ("-------------- Cadastrando Turma --------------")

    nome = request.form['nome']
    curso = request.form['curso']

    print(nome, curso)

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_turma(nome, curso)
        VALUES(?,?);
    """, (nome, curso))

    conn.commit()
    conn.close()

    return ("Cadastro de Turma realizado com sucesso!", 200)
# fim Recursos da aplicação tb_turma

# inicio Recursos da aplicação tb_disciplina

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return ("Listado com sucesso", 200)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina WHERE id_disciplina = ?;
    """, (id,))

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Listado com sucesso", 200)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():

    print ("-------------- Cadastrando Disciplina --------------")

    nome = request.form['nome']

    print(nome)

    conn = sqlite3.connect('EscolaServicoApp.db')

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_disciplina(nome)
        VALUES(?);
    """, (nome,))

    conn.commit()
    conn.close()

    return ("Cadastro de Disciplina realizado com sucesso!", 200)
# fim Recursos da aplicação tb_disciplina


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
