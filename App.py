from flask import Flask, request
import sqlite3
from flask import jsonify

app = Flask(__name__)
database = 'EscolaServicoApp.db'

@app.route("/")
def index():
    return ("Seja Bem vindo ao sistema de gerenciamento dos alunos matriculados, cursos, turmas e as disciplinas existentes no IFPB", 200)

# inicio Recursos da aplicação tb_escola

@app.route("/escolas", methods=['GET'])
def getEscola():

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_escola;
    """)
    escolas = list()
    for linha in cursor.fetchall():
        escola = {
            "id_escola": linha[0],
            "nome": linha[1],
            "logradouro": linha[2],
            "cidade": linha[3]
        }
        escolas.append(escola)

    conn.close()

    return jsonify(escolas)

    return ("Listado com sucesso", 200)


@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_escola WHERE id_escola = ?;
    """, (id,))

    linha = cursor.fetchone()
    escola = {
        "id_escola": linha[0],
        "nome": linha[1],
        "logradouro": linha[2],
        "cidade": linha[3]
    }
    conn.close()
    return jsonify(linha)
    return ("Listado com sucesso", 200)

@app.route("/escola", methods=['POST'])
def setEscola():

    print ("-------------- Cadastrando Escola --------------")
    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    print(nome, logradouro, cidade)

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?,?,?);
    """, (nome,logradouro, cidade))
    conn.commit()
    conn.close()

    id_escola = cursor.lastrowid
    escola["id_escola"] = id_escola

    return jsonify(escola)
# fim Recursos da aplicação tb_escola

# inicio Recursos da aplicação tb_aluno
@app.route("/alunos", methods=['GET'])
def getAluno():

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)
    alunos = list()
    for linha in cursor.fetchall():
        aluno = {
            "id_aluno" : linha[0],
            "nome" : linha[1],
            "matricula" : linha[2],
            "cpf" : linha[3],
            "nascimento" : linha[4]
        }
        alunos.append(aluno)
    conn.close()

    return jsonify(alunos)
    return ("Listado com sucesso", 200)


@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno WHERE id_aluno = ?;
    """, (id,))

    linha = cursor.fetchone()
    aluno = {
        "id_aluno" : linha[0],
        "nome" : linha[1],
        "matricula" : linha[2],
        "cpf" : linha[3],
        "nascimento" : linha[4]
    }
    conn.close()
    return jsonify(linha)
    return ("Listado com sucesso", 200)


@app.route("/aluno", methods=['POST'])
def setAluno():

    print ("-------------- Cadastrando Aluno --------------")
    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    print(nome, matricula, cpf, nascimento)

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?,?,?,?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno["id_aluno"] = id

    return jsonify(aluno)
    return ("Cadastro de Aluno realizado com sucesso!", 200)

# inicio Recursos da aplicação tb_aluno

# inicio Recursos da aplicação tb_curso

@app.route("/cursos", methods=['GET'])
def getCurso():

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso;
    """)

    cursos = list()

    for linha in cursor.fetchall():
        curso = {
            "id_curso" : linha[0],
            "nome" : linha[1],
            "turno" : linha[2]
        }
        cursos.append(curso)

    conn.close()

    return jsonify(cursos)

    return ("Listado com sucesso", 200)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso WHERE id_curso = ?;
    """, (id,))

    linha = cursor.fetchone()
    curso = {
        "id_curso" : linha[0],
        "nome" : linha[1],
        "turno" : linha[2]
    }
    conn.close()

    return jsonify(curso)
    return ("Listado com sucesso", 200)

@app.route("/curso", methods=['POST'])
def setCurso():

    print ("-------------- Cadastrando Curso --------------")
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    print(nome, turno)

    conn = sqlite3.connect('EscolaServicoApp.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?,?);
    """, (nome, turno))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno["id_curso"] = id

    return jsonify(curso)

    return ("Cadastro de Curso realizado com sucesso!", 200)
# fim Recursos da aplicação tb_curso

# inicio Recursos da aplicação tb_turma

@app.route("/turmas", methods=['GET'])
def getTurmas():

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma;
    """)

    turmas = list()
    for linha in cursor.fetchall():
        turma = {
            "id_turma" : linha[0],
            "nome" : linha[1],
            "curso" : linha[2]
        }
        turmas.append(turma)

    conn.close()
    return jsonify(turmas)

    return ("Listado com sucesso", 200)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma WHERE id_turma = ?;
    """, (id,))

    linha = cursor.fetchone()
    turma = {
        "id_turma" : linha[0],
        "nome" : linha[1],
        "curso" : linha[2]
    }
    conn.close()

    return jsonify(linha)
    return ("Listado com sucesso", 200)

@app.route("/turma", methods=['POST'])
def setTurma():

    print ("-------------- Cadastrando Turma --------------")
    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']

    print(nome, curso)

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_turma(nome, curso)
        VALUES(?,?);
    """, (nome, curso))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno["id_curso"] = id

    return jsonify(turma)
    return ("Cadastro de Turma realizado com sucesso!", 200)
# fim Recursos da aplicação tb_turma

# inicio Recursos da aplicação tb_disciplina

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina;
    """)

    disciplinas = list()
    for linha in cursor.fetchall():
        disciplina = {
            "id_disciplina" : linha[0],
            "nome" : linha[1]
        }
        disciplinas.append(disciplina)
    conn.close()

    return jsonify(disciplinas)

    return ("Listado com sucesso", 200)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina WHERE id_disciplina = ?;
    """, (id,))

    linha = cursor.fetchone()
    disciplina = {
        "id_disciplina" : linha[0],
        "nome" : linha[1]
    }
    conn.close()
    return jsonify(linha)
    return ("Listado com sucesso", 200)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():

    print ("-------------- Cadastrando Disciplina --------------")
    disciplina = request.get_json()
    nome = disciplina['nome']

    print(nome)

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_disciplina(nome)
        VALUES(?);
    """, (nome,))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno["id_disciplina"] = id

    return jsonify(disciplina)

    return ("Cadastro de Disciplina realizado com sucesso!", 200)
# fim Recursos da aplicação tb_disciplina

#INICIO DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db

@app.route("/escola", methods=['PUT'])
def updateEscola():
    print ("-------------- Atualizando Escola --------------")

@app.route("/aluno", methods=['PUT'])
def updateAluno():
    print ("-------------- Atualizando Aluno --------------")

@app.route("/curso", methods=['PUT'])
def updateCurso():
    print ("-------------- Atualizando Curso --------------")

@app.route("/turma", methods=['PUT'])
def updateTurma():
    print ("-------------- Atualizando Turma --------------")

@app.route("/disciplina", methods=['PUT'])
def updateDisciplina(id):
    print ("-------------- Atualizando Disciplina --------------")
    # Receber o JSON.
    disciplina = request.get_json()
    nome = disciplina['nome']
    # Buscar a disciplina pelo "id".
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM tb_disciplina WHERE id_disciplina = ?""", (id,))
    # Atualizar os dados caso o aluno seja encontrado através do "id".
    cursor.execute("""
        UPDATE tb_disciplina SET nome = ? WHERE id_disciplina = ?;
    """, (nome,id))
    #Retornar o JSON do aluno atualizado.

    conn.commit()
    conn.close()

    return ("PUT", 200)
#FIM DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
