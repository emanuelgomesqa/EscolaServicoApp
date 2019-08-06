from flask import Flask
from flask_json_schema import JsonSchema, JsonValidationError
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


#Validação
schema = JsonSchema()
schema.init_app(app)

schema_escola = {
    'required': ['nome', 'logradouro', 'cidade'],
    'properties': {
        'nome': {'type': 'string'},
        'logradouro': {'type': 'string'},
        'cidade': {'type': 'string'}
    }
}

schema_aluno = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'}
    }
}

schema_curso = {
    'required': ['nome','turno'],
    'properties': {
        'nome': {'type': 'string'},
        'turno': {'type': 'string'}
    }
}

schema_turma = {
    'required': ['nome','curso'],
    'properties': {
        'nome': {'type': 'string'},
        'curso': {'type': 'string'}
    }
}

schema_disciplina = {
    'required': ['nome'],
    'properties': {
        'nome': {'type': 'string'}
    }
}


database = 'EscolaServicoApp.db'

@app.route("/")
def index():
    return ("Seja Bem vindo ao sistema de gerenciamento dos alunos matriculados, cursos, turmas e as disciplinas existentes no IFPB", 200)

# Inicio de Listar todos os itens nas tabelas -------------------------------------------------------------------------------------

@app.route("/escolas", methods=['GET'])
def getEscola():
    logger.info("Listando Escolas")
    try:
<<<<<<< HEAD
        conn = sqlite3.connect(database)
=======
        conn = sqlite3.connect(data)
>>>>>>> 0f84e2fa774e77fb9fc20fc131aaa7a41089f779
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
<<<<<<< HEAD
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Escolas")
=======
    except(sqlite3.Error):
        logger.Error("existe um erro no método Escolas")

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
>>>>>>> 0f84e2fa774e77fb9fc20fc131aaa7a41089f779

    return jsonify(escolas)

@app.route("/alunos", methods=['GET'])
def getAluno():
    logger.info("Listando Alunos")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_aluno; """)
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
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Alunos")

    return jsonify(alunos)

@app.route("/cursos", methods=['GET'])
def getCurso():
    logger.info("Listando Cursos")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_curso; """)
        cursos = list()
        for linha in cursor.fetchall():
            curso = {
                "id_curso" : linha[0],
                "nome" : linha[1],
                "turno" : linha[2]
            }
            cursos.append(curso)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Cursos")

    return jsonify(cursos)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando Turmas")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turma; """)
        turmas = list()
        for linha in cursor.fetchall():
            turma = {
                "id_turma" : linha[0],
                "nome" : linha[1],
                "curso" : linha[2]
            }
            turmas.append(turma)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Turmas")

    return jsonify(turmas)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando Disciplinas")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_disciplina; """)
        disciplinas = list()
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina" : linha[0],
                "nome" : linha[1]
            }
            disciplinas.append(disciplina)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Disciplinas")

    return jsonify(disciplinas)

# Fim de Listar todos os itens nas tabelas    -------------------------------------------------------------------------------------

# Inicio de Listar todos os itens nas tabelas -------------------------------------------------------------------------------------

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):
    logger.info("Listando escola com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id, ))
        linha = cursor.fetchone()
        escola = {
            "id_escola":linha[0],
            "nome":linha[1],
            "logradouro":linha[2],
            "cidade":linha[3]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Escola com ID %s" %(id))

    return jsonify(escola)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    logger.info("Listando Alunos com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_aluno WHERE id_aluno = ?; """, (id,))
        linha = cursor.fetchone()
        aluno = {
            "id_aluno" : linha[0],
            "nome" : linha[1],
            "matricula" : linha[2],
            "cpf" : linha[3],
            "nascimento" : linha[4]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Aluno com ID %s" %(id))

    return jsonify(linha)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    logger.info("Listando Cursos com ID  %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_curso WHERE id_curso = ?; """, (id,))
        linha = cursor.fetchone()
        curso = {
            "id_curso" : linha[0],
            "nome" : linha[1],
            "turno" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Curso com ID %s" %(id))

    return jsonify(curso)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    logger.info("Listando Turmas com ID  %d" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turma WHERE id_turma = ?; """, (id,))
        linha = cursor.fetchone()
        turma = {
            "id_turma" : linha[0],
            "nome" : linha[1],
            "curso" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Turma com ID %s" %(id))

    return jsonify(linha)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    logger.info("Listando Disciplina com ID  %d" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_disciplina WHERE id_disciplina = ?; """, (id,))
        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina" : linha[0],
            "nome" : linha[1]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Disciplina com ID %s" %(id))

    return jsonify(linha)
# Fim de Listar todos os itens nas tabelas -------------------------------------------------------------------------------------

# Inicio de Cadastrar itens nas tabelas    -------------------------------------------------------------------------------------
@app.route("/escola", methods=['POST'])
@schema.validate(schema_escola)
def setEscola():
    logger.info("Cadastrando uma Nova Escola")
    try:
        escola = request.get_json()
        nome = escola['nome']
        logradouro = escola['logradouro']
        cidade = escola['cidade']
        print(nome, logradouro, cidade)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_escola(nome, logradouro, cidade) VALUES(?,?,?); """, (nome,logradouro, cidade))
        conn.commit()
        conn.close()
        id_escola = cursor.lastrowid
        escola["id_escola"] = id_escola
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de uma Escola")

    return jsonify(escola)

@app.route("/aluno", methods=['POST'])
@schema.validate(schema_aluno)
def setAluno():
    logger.info("Cadastrando um Novo Aluno")
    try:
        aluno = request.get_json()
        nome = aluno['nome']
        matricula = aluno['matricula']
        cpf = aluno['cpf']
        nascimento = aluno['nascimento']
        print(nome, matricula, cpf, nascimento)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_aluno(nome, matricula, cpf, nascimento) VALUES(?,?,?,?); """, (nome, matricula, cpf, nascimento))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        aluno["id_aluno"] = id
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de um Aluno")

    return jsonify(aluno)

@app.route("/curso", methods=['POST'])
@schema.validate(schema_curso)
def setCurso():
    logger.info("Cadastrando um Novo Curso")
    try:
        curso = request.get_json()
        nome = curso['nome']
        turno = curso['turno']
        logger.info("Cadastrando um Novo Curso")
        conn = sqlite3.connect('EscolaServicoApp.db')
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_curso(nome, turno) VALUES(?,?); """, (nome, turno))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        curso["id_curso"] = id
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de um Curso")

    return jsonify(curso)

@app.route("/turma", methods=['POST'])
@schema.validate(schema_turma)
def setTurma():
    logger.info("Cadastrando uma Nova Turma")
    try:
        turma = request.get_json()
        nome = turma['nome']
        curso = turma['curso']
        print(nome, curso)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_turma(nome, curso) VALUES(?,?); """, (nome, curso))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        turma["id_turma"] = id
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de uma Turma")

    return jsonify(turma)

@app.route("/disciplina", methods=['POST'])
@schema.validate(schema_disciplina)
def setDisciplina():
    logger.info("Cadastrando uma Nova Disciplina")
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        print(nome)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_disciplina(nome) VALUES(?); """, (nome,))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        disciplina["id_disciplina"] = id
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de uma Disciplina")

    return jsonify(disciplina)

# Fim de Cadastrar itens nas tabelas    -------------------------------------------------------------------------------------

#INICIO DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db -------------------------------------------------------------------------------------

@app.route("/escola/<int:id>", methods=['PUT'])
@schema.validate(schema_escola)
def updateEscola(id):
<<<<<<< HEAD
    logger.info("Atualizando Escola com ID: %s" %(id))
    try:
        escola = request.get_json()
        nome = escola['nome']
        logradouro = escola['logradouro']
        cidade = escola['cidade']
=======
    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']
    logger.info("Atualizando: %s, %s, %s" %(nome, logradouro, cidade))
    try:
>>>>>>> 0f84e2fa774e77fb9fc20fc131aaa7a41089f779
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
<<<<<<< HEAD
            logger.info("Atualizando uma Escola")
=======
            logger.info("Atualizando uma Nova Escola")
>>>>>>> 0f84e2fa774e77fb9fc20fc131aaa7a41089f779
            cursor.execute("""UPDATE tb_escola SET nome=?, logradouro=?, cidade=?""" (nome,logradouro, cidade, id))
            conn.commit()
        else:
            logger.info("Cadastrando uma Nova Escola")
            cursor.execute(""" INSERT INTO tb_escola(nome, logradouro, cidade) VALUES(?,?,?); """, (nome,logradouro, cidade))
            conn.commit()
            id = cursor.lastrowid
            escola["id_escola"] = id
<<<<<<< HEAD
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização da Escola com ID %s"%(id))

=======
    except(sqlite3.error):
        logger.error("existe um error")
    conn.close()
>>>>>>> 0f84e2fa774e77fb9fc20fc131aaa7a41089f779
    return jsonify(escola)
@app.route("/aluno/<int:id>", methods=['PUT'])
@schema.validate(schema_aluno)
def updateAluno(id):
    logger.info("Atualizando Aluno com ID: %s" %(id))
    try:
        aluno = request.get_json()
        nome = aluno['nome']
        matricula = aluno['matricula']
        cpf = aluno['cpf']
        nascimento = aluno['nascimento']
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
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização do Aluno com ID %s"%(id))

    return jsonify(aluno)
@app.route("/curso/<int:id>", methods=['PUT'])
@schema.validate(schema_curso)
def updateCurso(id):
    logger.info("Atualizando Curso com ID: %s" %(id))
    try:
        curso = request.get_json()
        nome = curso['nome']
        turno = curso['turno']
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
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização do Curso com ID %s"%(id))

    return jsonify(curso)
@app.route("/turma/<int:id>", methods=['PUT'])
@schema.validate(schema_turma)
def updateTurma(id):
    logger.info("Atualizando Turma com ID: %s" %(id))
    try:
        turma = request.get_json()
        nome = turma['nome']
        curso = turma['curso']
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
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização da Turma com ID %s"%(id))

    return jsonify(turma)
@app.route("/disciplina/<int:id>", methods=['PUT'])
@schema.validate(schema_disciplina)
def updateDisciplina(id):
    logger.info("Atualizando Disciplina com ID: %s" %(id))
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
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
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização da Disciplina com ID %s"%(id))

    return jsonify(disciplina)
#FIM DA IMPLEMENTAÇÃO DOS MÉTODOS PUT DAS TABELAS CRIADAS NO BANCO DE DADOS EscolaServicoApp.db -------------------------------------------------------------------------------------

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
