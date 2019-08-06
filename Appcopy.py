from flask import Flask
from flask import request
from flask import jsonify
import sqlite3
import logging

app = Flask(__name__)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaApp.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

database = 'EscolaServicoApp.db'

@app.route("/")
def index():
    return ("Seja Bem vindo ao sistema de gerenciamento dos alunos matriculados, cursos, turmas e as disciplinas existentes no IFPB", 200)
# inicio Recursos da aplicação tb_escola
@app.route("/escolas", methods=['GET'])
def getEscola():
    logger.info("Listando Escolas")
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_escola; """)
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
    logger.info("Listando Escola com ID  %d" %(id))
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
    logger.info("Cadastrando uma Nova Escola")
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
    logger.info("Listando Alunos")
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
    logger.info("Listando Alunos com ID  %d" %(id))
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
    logger.info("Cadastrando um Novo Aluno")
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
    logger.info("Listando Cursos")
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
    logger.info("Listando Cursos com ID  %d" %(id))
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
    logger.info("Cadastrando um Novo Curso")
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    logger.info("Cadastrando um Novo Curso")
    conn = sqlite3.connect('EscolaServicoApp.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?,?);
    """, (nome, turno))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    curso["id_curso"] = id

    return jsonify(curso)

    return ("Cadastro de Curso realizado com sucesso!", 200)
# fim Recursos da aplicação tb_curso

# inicio Recursos da aplicação tb_turma

@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando Turmas")
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
    logger.info("Listando Turmas com ID  %d" %(id))
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
    logger.info("Cadastrando uma Nova Turma")
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
    turma["id_turma"] = id

    return jsonify(turma)
    return ("Cadastro de Turma realizado com sucesso!", 200)
# fim Recursos da aplicação tb_turma

# inicio Recursos da aplicação tb_disciplina

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando Disciplinas")
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
    logger.info("Listando Disciplina com ID  %d" %(id))
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
    logger.info("Cadastrando uma Nova Disciplina")
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
    disciplina["id_disciplina"] = id

    return jsonify(disciplina)

    return ("Cadastro de Disciplina realizado com sucesso!", 200)
# fim Recursos da aplicação tb_disciplina

#INICIO DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db

@app.route("/escola/<int:id>", methods=['PUT'])
def updateEscola(id):
    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']
    logger.info("Atualizando: %s, %s, %s" %(nome, logradouro, cidade))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        logger.info("Atualizando uma Escola")
        cursor.execute("""UPDATE tb_escola SET nome=?, logradouro=?, cidade=?""" (nome,logradouro, cidade, id))
        conn.commit()
    else:
        logger.info("Cadastrando uma Nova Escola")
        cursor.execute(""" INSERT INTO tb_escola(nome, logradouro, cidade) VALUES(?,?,?); """, (nome,logradouro, cidade))
        conn.commit()
        id = cursor.lastrowid
        escola["id_escola"] = id
    conn.close()
    return jsonify(escola)
@app.route("/aluno/<int:id>", methods=['PUT'])
def updateAluno(id):
    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']
    logger.info("Atualizando: %s, %s, %s, %s" %(nome, matricula, cpf, nascimento))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_aluno WHERE id_aluno = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        logger.info("Atualizando um Aluno")
        cursor.execute("""UPDATE tb_aluno SET nome=?, matricula=?, cpf=?,nascimento=? WHERE id_aluno = ? """, (nome, matricula, cpf, nascimento,id))
        conn.commit()
    else:
        logger.info("Cadastrando um Novo Aluno")
        cursor.execute(""" INSERT INTO tb_aluno(nome, matricula, cpf, nascimento) VALUES(?,?,?,?); """, (nome, matricula, cpf, nascimento))
        conn.commit()
        id = cursor.lastrowid
        aluno["id_aluno"] = id
    conn.close()
    return jsonify(aluno)
@app.route("/curso/<int:id>", methods=['PUT'])
def updateCurso(id):
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    logger.info("Atualizando: %s, %s" %(nome,turno))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_curso WHERE id_curso = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        logger.info("Atualizando um Curso")
        cursor.execute("""UPDATE tb_curso SET nome=?, turno=? WHERE id_curso = ? """, (nome, turno, id))
        conn.commit()
    else:
        logger.info("Cadastrando um Novo Curso")
        cursor.execute(""" INSERT INTO tb_curso(nome, turno) VALUES(?,?); """, (nome, turno))
        conn.commit()
        id = cursor.lastrowid
        curso["id_curso"] = id
    conn.close()
    return jsonify(curso)
@app.route("/turma/<int:id>", methods=['PUT'])
def updateTurma(id):
    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']
    logger.info("Atualizando: %s, %s" %(nome,curso))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_turma WHERE id_turma = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        logger.info("Atualizando uma Turma")
        cursor.execute(""" UPDATE tb_turma SET nome=?, curso=? WHERE id_disciplina = ?""", (nome,curso, id))
        conn.commit()
    else:
        logger.info("Cadastrando uma Nova Turma")
        cursor.execute(""" INSERT INTO tb_turma(nome, curso) VALUES(?,?); """, (nome, curso))
        conn.commit()
        id = cursor.lastrowid
        turma["id_turma"] = id
    conn.close()
    return jsonify(turma)
@app.route("/disciplina/<int:id>", methods=['PUT'])
def updateDisciplina(id):
    disciplina = request.get_json()
    nome = disciplina['nome']
    logger.info("Atualizando: %s" %(nome))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_disciplina WHERE id_disciplina = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        logger.info("Atualizando uma Disciplina")
        cursor.execute(""" UPDATE tb_disciplina SET nome=? WHERE id_disciplina = ?""", (nome, id))
        conn.commit()
    else:
        logger.info("Cadastrando uma Nova Disciplina")
        cursor.execute(""" INSERT INTO tb_disciplina(nome) VALUES(?); """, (nome,))
        conn.commit()
        id = cursor.lastrowid
        disciplina["id_disciplina"] = id
    conn.close()
    return jsonify(disciplina)
#FIM DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
