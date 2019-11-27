from flask import Flask
from flask_json_schema import JsonSchema, JsonValidationError
from flask import request
from flask import jsonify
import sqlite3
import logging
from flask_cors import CORS

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

schema_endereco = {
    'required': ['logradouro', 'complemento',  'bairro', 'cep', 'numero'],
    'properties': {
        'logradouro': {'type': 'string'},
        'complemento': {'type': 'string'},
        'bairro': {'type': 'string'},
        'cep': {'type': 'string'},
        'numero': {'type': 'integer'}
    }
}

schema_escola = {
    'required': ['nome', 'fk_id_endereco', 'fk_id_campus'],
    'properties': {
        'nome': {'type': 'string'},
        'id_endereco': {'type': 'integer'},
        'id_campus': {'type': 'integer'}
    }
}

schema_aluno = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento', 'fk_id_endereco', 'fk_id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'},
        'id_endereco': {'type': 'integer'},
        'id_curso': {'type': 'integer'}
    }
}

schema_professor = {
    'required': ['nome', 'fk_id_endereco'],
    'properties': {
        'nome': {'type': 'string'},
        'id_endereco': {'type': 'integer'}
    }
}

schema_disciplina = {
    'required': ['nome', 'fk_id_professor'],
    'properties': {
        'nome': {'type': 'string'},
        'id_professor': {'type': 'integer'}
    }
}

schema_curso = {
    'required': ['nome','fk_id_turno'],
    'properties': {
        'nome': {'type': 'string'},
        'id_turno': {'type': 'integer'}
    }
}

schema_campus = {
    'required': ['sigla','cidade'],
    'properties': {
        'sigla': {'type': 'string'},
        'cidade': {'type': 'string'}
    }
}

schema_turma = {
    'required': ['nome','fk_id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'id_curso': {'type': 'integer'}
    }
}

schema_turno = {
    'required': ['nome'],
    'properties': {
        'nome': {'type': 'string'}
    }
}



database = 'EscolaApp_versao2.db'

@app.route("/")
def index():
    return ("Projeto do Serviço Aplicação Escola Versão 2.0. Discentes: Emanuel Gomes e Maria Vitória", 200)

# Inicio de Listar todos os itens nas tabelas -------------------------------------------------------------------------------------

@app.route("/enderecos", methods=['GET'])
def getEndereco():
    logger.info("Listando Todos os Endereços")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_endereco; """)
        enderecos = list()
        for linha in cursor.fetchall():
            endereco = {
                "idtb_endereco": linha[0],
                "logradouro": linha[1],
                "complemento": linha[2],
                "bairro": linha[3],
                "cep": linha[4],
                "numero": linha[5]
            }
            enderecos.append(endereco)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Endereços")

    return jsonify(enderecos)

@app.route("/campi", methods=['GET'])
def getCampus():
    logger.info("Listando Todos os Campus")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_campus; """)
        campus = list()
        for linha in cursor.fetchall():
            campi = {
                "id_campus": linha[0],
                "sigla": linha[1],
                "cidade": linha[2]
            }
            campus.append(campi)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Campi")

    return jsonify(campus)

@app.route("/escolas", methods=['GET'])
def getEscola():
    logger.info("Listando Todas as Escolas")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_escola; """)
        escolas = list()
        for linha in cursor.fetchall():
            escola = {
                "id_escola": linha[0],
                "nome": linha[1],
                "id_endereco": linha[2],
                "id_campus": linha[3]
            }
            escolas.append(escola)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Escolas")

    return jsonify(escolas)

@app.route("/alunos", methods=['GET'])
def getAluno():
    logger.info("Listando Todos os Alunos")
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
                "nascimento" : linha[4],
                "id_endereco": linha[5],
                "id_curso": linha[6]
            }
            alunos.append(aluno)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Alunos")

    return jsonify(alunos)

@app.route("/professores", methods=['GET'])
def getProfessores():
    logger.info("Listando Todos os Professores")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_professor; """)
        professores = list()
        for linha in cursor.fetchall():
            professor = {
                "id_professor" : linha[0],
                "nome" : linha[1],
                "id_endereco": linha[2]
            }
            professores.append(professor)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Alunos")

    return jsonify(professores)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando Todas as Disciplinas")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_disciplina; """)
        disciplinas = list()
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina" : linha[0],
                "nome" : linha[1],
                "id_professor": linha[2]
            }
            disciplinas.append(disciplina)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Disciplinas")

    return jsonify(disciplinas)

@app.route("/turnos", methods=['GET'])
def getTurnos():
    logger.info("Listando Todos os Turnos")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turno; """)
        turnos = list()
        for linha in cursor.fetchall():
            turno = {
                "id_turno" : linha[0],
                "nome" : linha[1]
            }
            turnos.append(turno)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Alunos")

    return jsonify(turnos)

@app.route("/cursos", methods=['GET'])
def getCurso():
    logger.info("Listando Todos os Cursos")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_curso; """)
        cursos = list()
        for linha in cursor.fetchall():
            curso = {
                "id_curso" : linha[0],
                "nome" : linha[1],
                "id_turno": linha[2]
            }
            cursos.append(curso)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem dos Cursos")

    return jsonify(cursos)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando Todas as Turmas")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turma; """)
        turmas = list()
        for linha in cursor.fetchall():
            turma = {
                "id_turma" : linha[0],
                "nome" : linha[1],
                "id_curso" : linha[2]
            }
            turmas.append(turma)
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem das Turmas")

    return jsonify(turmas)

# Fim de Listar todos os itens nas tabelas ----------------------------------------------------------------------------------------

# Inicio de Listar os itens por ID das tabelas ------------------------------------------------------------------------------------

@app.route("/enderecos/<int:id>", methods=['GET'])
def getEnderecoById(id):
    logger.info("Listando o Endereço com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_endereco WHERE idtb_endereco = ?; """, (id, ))
        linha = cursor.fetchone()
        endereco = {
            "idtb_endereco": linha[0],
            "logradouro": linha[1],
            "complemento": linha[2],
            "bairro": linha[3],
            "cep": linha[4],
            "numero": linha[5]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Endereço com ID %s" %(id))

    return jsonify(endereco)

@app.route("/campi/<int:id>", methods=['GET'])
def getCampusById(id):
    logger.info("Listando o Campi com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_campus WHERE id_campus = ?; """, (id, ))
        linha = cursor.fetchone()
        campi = {
            "id_campus": linha[0],
            "sigla": linha[1],
            "cidade": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Campi com ID %s" %(id))

    return jsonify(campi)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaById(id):
    logger.info("Listando a Escola com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id, ))
        linha = cursor.fetchone()
        escola = {
            "id_escola": linha[0],
            "nome": linha[1],
            "id_endereco": linha[2],
            "id_campus": linha[3]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Escola com ID %s" %(id))

    return jsonify(escola)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunoById(id):
    logger.info("Listando o Aluno com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_aluno WHERE id_aluno = ?; """, (id, ))
        linha = cursor.fetchone()
        aluno = {
            "id_aluno" : linha[0],
            "nome" : linha[1],
            "matricula" : linha[2],
            "cpf" : linha[3],
            "nascimento" : linha[4],
            "id_endereco": linha[5],
            "id_curso": linha[6]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Aluno com ID %s" %(id))

    return jsonify(aluno)

@app.route("/professores/<int:id>", methods=['GET'])
def getProfessoresById(id):
    logger.info("Listando o Professor com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_professor WHERE id_professor = ?; """, (id, ))
        linha = cursor.fetchone()
        professor = {
            "id_professor" : linha[0],
            "nome" : linha[1],
            "id_endereco": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Professor com ID %s" %(id))

    return jsonify(professor)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasById(id):
    logger.info("Listando a disciplina com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_disciplina WHERE id_disciplina = ?; """, (id, ))
        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina" : linha[0],
            "nome" : linha[1],
            "id_professor": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Disciplina com ID %s" %(id))

    return jsonify(disciplina)

@app.route("/turnos/<int:id>", methods=['GET'])
def getTurnosById(id):
    logger.info("Listando o turno com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turno WHERE id_turno = ?; """, (id, ))
        linha = cursor.fetchone()
        turno = {
            "id_turno" : linha[0],
            "nome" : linha[1]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Turno com ID %s" %(id))

    return jsonify(turno)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursoById(id):
    logger.info("Listando o Curso com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_curso; """)
        linha = cursor.fetchone()
        curso = {
            "id_curso" : linha[0],
            "nome" : linha[1],
            "id_turno": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem do Curso com ID %s" %(id))

    return jsonify(curso)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasById(id):
    logger.info("Listando a Turma com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turma; """)
        linha = cursor.fetchone()
        turma = {
            "id_turma" : linha[0],
            "nome" : linha[1],
            "id_curso" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um erro na Listagem da Turma com ID %s" %(id))

    return jsonify(turma)

# Fim de Listar os itens por ID das tabelas ---------------------------------------------------------------------------------------

# Inicio de Cadastrar os itens das Tabelas ----------------------------------------------------------------------------------------

@app.route("/endereco", methods=['POST'])
@schema.validate(schema_endereco)
def setEndereco():
    logger.info("Cadastrando um Novo Endereço")
    try:
        endereco = request.get_json()
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cep = endereco['cep']
        numero = endereco['numero']
        print(logradouro, complemento, bairro, cep, numero)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero) VALUES(?,?,?,?,?); """, (logradouro, complemento, bairro, cep, numero))
        conn.commit()
        conn.close()
        id_endereco = cursor.lastrowid
        endereco["id_endereco"] = id_endereco
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(endereco)

@app.route("/campus", methods=['POST'])
@schema.validate(schema_campus)
def setCampus():
    logger.info("Cadastrando um Novo Campus")
    try:
        campus = request.get_json()
        sigla = campus['sigla']
        cidade = campus['cidade']
        print(sigla, cidade)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_campus(sigla, cidade) VALUES(?,?); """, (sigla, cidade))
        conn.commit()
        conn.close()
        id_campus = cursor.lastrowid
        campus["id_campus"] = id_campus
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(campus)

@app.route("/escola", methods=['POST'])
@schema.validate(schema_escola)
def setEscola():
    logger.info("Cadastrando uma Nova Escola")
    try:
        escola = request.get_json()
        nome = escola['nome']
        id_endereco = escola['fk_id_endereco']
        id_campus = escola['fk_id_campus']
        print(nome, id_endereco, id_campus)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus) VALUES(?,?,?); """, (nome, id_endereco, id_campus))
        conn.commit()
        conn.close()
        id_escola = cursor.lastrowid
        escola["id_escola"] = id_escola
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(escola)

@app.route("/aluno", methods=['POST'])
@schema.validate(schema_aluno)
def setAluno():
    logger.info("Cadastrando um Novo Aluno")
    try:
        aluno = request.get_json()
        print(aluno)
        nome = aluno['nome']
        print(nome)
        matricula = aluno['matricula']
        print(matricula)
        cpf = aluno['cpf']
        print(cpf)
        nascimento = aluno['nascimento']
        print(nascimento)
        id_endereco = aluno['fk_id_endereco']
        print(id_endereco)
        id_curso = aluno['fk_id_curso']
        print(id_curso)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso) VALUES(?,?,?,?,?,?); """, (nome, matricula, cpf, nascimento, id_endereco, id_curso))
        conn.commit()
        conn.close()
        id_aluno = cursor.lastrowid
        aluno["id_aluno"] = id_aluno
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(aluno)

@app.route("/professor", methods=['POST'])
@schema.validate(schema_professor)
def setProfessor():
    logger.info("Cadastrando um Novo Professor")
    try:
        professor = request.get_json()
        nome = professor['nome']
        id_endereco = professor['fk_id_endereco']
        print(nome, id_endereco)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_professor(nome, fk_id_endereco) VALUES(?,?); """, (nome, id_endereco))
        conn.commit()
        conn.close()
        id_professor = cursor.lastrowid
        professor["id_professor"] = id_professor
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(professor)

@app.route("/disciplina", methods=['POST'])
@schema.validate(schema_disciplina)
def setDisciplina():
    logger.info("Cadastrando uma Nova Disciplina")
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        id_professor = disciplina['fk_id_professor']
        print(nome, id_professor)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_disciplina(nome, fk_id_professor) VALUES(?,?); """, (nome, id_professor))
        conn.commit()
        conn.close()
        id_disciplina = cursor.lastrowid
        disciplina["id_disciplina"] = id_disciplina
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(disciplina)

@app.route("/turno", methods=['POST'])
@schema.validate(schema_turno)
def setTurno():
    logger.info("Cadastrando um Novo Turno")
    try:
        turno = request.get_json()
        nome = turno['nome']
        print(nome)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_turno(nome) VALUES(?); """, (nome, ))
        conn.commit()
        conn.close()
        id_turno = cursor.lastrowid
        turno["id_turno"] = id_turno
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(turno)

@app.route("/curso", methods=['POST'])
@schema.validate(schema_curso)
def setCurso():
    logger.info('Cadastrando um Novo curso')

    try:
        curso = request.get_json()
        nome = curso["nome"]
        id_turno = curso["fk_id_turno"]
        print (nome, id_turno)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_curso(nome, fk_id_turno) VALUES(?, ?); """, (nome,id_turno))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        curso['id_curso'] = id

    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(curso)

@app.route("/turma", methods=['POST'])
@schema.validate(schema_turma)
def setTurma():
    logger.info("Cadastrando uma Nova Turma")
    try:
        turma = request.get_json()
        nome = turma['nome']
        id_curso = turma['fk_id_curso']
        print(nome, id_curso)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO tb_turma(nome, fk_id_curso) VALUES(?,?); """, (nome, id_curso))
        conn.commit()
        conn.close()
        id_turma = cursor.lastrowid
        turma["id_turma"] = id_turma
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(turma)

# Fim de Cadastrar os itens das Tabelas -------------------------------------------------------------------------------------------

# Inicio de Atualizar os itens das Tabelas ----------------------------------------------------------------------------------------

@app.route("/endereco/<int:id>", methods=['PUT'])
@schema.validate(schema_endereco)
def updateEndereco(id):
    logger.info("Atualizando Endereco com ID: %s" %(id))
    try:
        endereco = request.get_json()
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cep = endereco['cep']
        numero = endereco['numero']

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_endereco WHERE id_endereco = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Endereço")
            cursor.execute("""
                UPDATE tb_endereco
                SET logradouro=?, complemento=?, bairro=?, cep=?, numero=?
                where id_endereco = ?
                """, (logradouro,complemento, bairro, cep, numero, id))
            print(logradouro, complemento, bairro, cep, numero)
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Endereço")
            cursor.execute(""" INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero) VALUES(?,?,?,?,?); """, (logradouro, complemento, bairro, cep, numero))
            conn.commit()
            id_endereco = cursor.lastrowid
            endereco["id_endereco"] = id_endereco
        conn.close()
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(endereco)

@app.route("/campus/<int:id>", methods=['PUT'])
@schema.validate(schema_campus)
def updateCampus(id):
    logger.info("Atualizando Campus com ID: %s" %(id))
    try:
        campus = request.get_json()
        sigla = campus['sigla']
        cidade = campus['cidade']
        print(sigla, cidade)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_campus WHERE id_campus = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Campus")
            cursor.execute("""
                UPDATE tb_campus
                SET sigla=?, cidade=?
                WHERE id_campus = ?
                """, (sigla, cidade, id))
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Campus")
            cursor.execute(""" INSERT INTO tb_campus(sigla, cidade) VALUES(?,?); """, (sigla, cidade))
            conn.commit()
            id_campus = cursor.lastrowid
            campus["id_campus"] = id_campus
        conn.close()
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

    return jsonify(campus)

@app.route("/escola/<int:id>", methods=['PUT'])
@schema.validate(schema_escola)
def updateEscola(id):
    logger.info("Atualizando Escola com ID: %s" %(id))
    try:
        escola = request.get_json()
        nome = escola['nome']
        fk_id_endereco = escola['fk_id_endereco']
        fk_id_campus = escola['fk_id_campus']
        print(nome, fk_id_endereco, fk_id_campus)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando uma Escola")
            cursor.execute(""" UPDATE tb_escola SET nome=?, fk_id_endereco=?, fk_id_campus=? where id_escola =? """, (nome, fk_id_endereco, fk_id_campus, id))
            conn.commit()
        else:
            logger.info("Cadastrando uma Nova Escola")
            cursor.execute(""" INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus) VALUES(?,?,?); """, (nome, fk_id_endereco, fk_id_campus))
            conn.commit()
            id_escola = cursor.lastrowid
            escola["id_escola"] = id_escola
        conn.close()
    except(sqlite3.Error, Exception) as e:
        logger.error("Houve algum erro!")
        logger.error("Exception error: %s" %e)

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
        fk_id_endereco = aluno['fk_id_endereco']
        fk_id_curso = aluno['fk_id_curso']
        print(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_aluno WHERE id_aluno = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Aluno")
            cursor.execute("""UPDATE tb_aluno SET nome=?, matricula=?, cpf=?, nascimento=?, fk_id_endereco=?, fk_id_curso=? WHERE id_aluno = ? """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso, id))
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Aluno")
            cursor.execute(""" INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso) VALUES(?,?,?,?,?,?); """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso))
            conn.commit()
            id_aluno = cursor.lastrowid
            aluno["id_aluno"] = id_aluno
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização do Aluno com ID %s"%(id))

    return jsonify(aluno)

@app.route("/professor/<int:id>", methods=['PUT'])
@schema.validate(schema_professor)
def updateProfessor(id):
    logger.info("Atualizando Professor com ID: %s" %(id))
    try:
        professor = request.get_json()
        nome = professor['nome']
        fk_id_endereco = professor['fk_id_endereco']
        print(nome, fk_id_endereco)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_professor WHERE id_professor = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Professor")
            cursor.execute("""UPDATE tb_professor SET nome=?, fk_id_endereco=? WHERE id_professor = ? """, (nome, fk_id_endereco, id))
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Professor")
            cursor.execute(""" INSERT INTO tb_professor(nome, fk_id_endereco) VALUES(?,?); """, (nome, fk_id_endereco))
            conn.commit()
            id_professor = cursor.lastrowid
            professor["id_professor"] = id_professor
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização do Professor com ID %s"%(id))

    return jsonify(professor)

@app.route("/disciplina/<int:id>", methods=['PUT'])
@schema.validate(schema_disciplina)
def updateDisciplina(id):
    logger.info("Atualizando Disciplina com ID: %s" %(id))
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        fk_id_professor = disciplina['fk_id_professor']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_disciplina WHERE id_disciplina = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando uma Disciplina")
            cursor.execute(""" UPDATE tb_disciplina SET nome=?, fk_id_professor=? WHERE id_disciplina = ?""", (nome,fk_id_professor, id))
            conn.commit()
        else:
            logger.info("Cadastrando uma Nova Disciplina")
            cursor.execute(""" INSERT INTO tb_disciplina(nome, fk_id_professor) VALUES(?,?); """, (nome,fk_id_professor))
            conn.commit()
            id_disciplina = cursor.lastrowid
            disciplina["id_disciplina"] = id_disciplina
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização da Disciplina com ID %s"%(id))

    return jsonify(disciplina)

@app.route("/turno/<int:id>", methods=['PUT'])
@schema.validate(schema_turno)
def updateTurno(id):
    logger.info("Atualizando Turno com ID: %s" %(id))
    try:
        turno = request.get_json()
        nome = turno['nome']
        print(nome)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turno WHERE id_turno = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Turno")
            cursor.execute("""UPDATE tb_turno SET nome=? WHERE id_turno = ? """, (nome, id))
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Turno")
            cursor.execute(""" INSERT INTO tb_turno(nome) VALUES(?); """, (nome, ))
            conn.commit()
            id_turno = cursor.lastrowid
            turno["id_turno"] = id_turno
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização do Turno com ID %s"%(id))

    return jsonify(turno)

@app.route("/curso/<int:id>", methods=['PUT'])
@schema.validate(schema_curso)
def updateCurso(id):
    logger.info("Atualizando Curso com ID: %s" %(id))
    try:
        curso = request.get_json()
        nome = curso['nome']
        fk_id_turno = curso['fk_id_turno']
        print (nome, fk_id_turno)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_curso WHERE id_curso = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando um Curso")
            cursor.execute("""UPDATE tb_curso SET nome=?, fk_id_turno=? WHERE id_curso = ? """, (nome, fk_id_turno, id))
            conn.commit()
        else:
            logger.info("Cadastrando um Novo Curso")
            cursor.execute(""" INSERT INTO tb_curso(nome, fk_id_turno) VALUES(?,?); """, (nome, fk_id_turno))
            conn.commit()
            id_curso = cursor.lastrowid
            curso["id_curso"] = id_curso
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
        fk_id_curso = turma['fk_id_curso']
        print(nome, fk_id_curso)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM tb_turma WHERE id_turma = ?; """, (id,))
        data = cursor.fetchone()
        if (data is not None):
            logger.info("Atualizando uma Turma")
            cursor.execute(""" UPDATE tb_turma SET nome=?, fk_id_curso=? WHERE id_turma = ?""", (nome, fk_id_curso, id))
            conn.commit()
        else:
            logger.info("Cadastrando uma Nova Turma")
            cursor.execute(""" INSERT INTO tb_turma(nome, fk_id_curso) VALUES(?,?); """, (nome, fk_id_curso))
            conn.commit()
            id = cursor.lastrowid
            turma["id_turma"] = id
        conn.close()
    except(sqlite3.Error):
        logger.error("Houve um Erro na Atualização da Turma com ID %s"%(id))

    return jsonify(turma)

# Fim de Atualizar os itens das Tabelas -------------------------------------------------------------------------------------------

cors = CORS(app, resources={r"/*": {"origins": "*"}})

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000',debug=True, use_reloader=True)
