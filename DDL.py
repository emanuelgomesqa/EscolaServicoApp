import sqlite3

conn = sqlite3.connect('EscolaApp_versao2.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_endereco(
        id_endereco INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        logradouro VARCHAR(65) NOT NULL,
        complemento VARCHAR(45) NOT NULL,
        bairro VARCHAR(45) NOT NULL,
        cep VARCHAR(8) NOT NULL,
        numero INTEGER NOT NULL
    )
""")

print('tabela "tb_endereco" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_escola(
        id_escola INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        fk_id_endereco INTEGER NOT NULL,
        fk_id_campus INTEGER NOT NULL
    );
""")

print('tabela "tb_escola" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        matricula VARCHAR(12) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        nascimento DATE NOT NULL,
        fk_id_endereco INTEGER NOT NULL,
        fk_id_curso INTEGER NOT NULL
    );
""")

print('tabela "tb_aluno" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_professor(
        id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        fk_id_endereco INTEGER NOT NULL
    )
""")

print('tabela "tb_professor" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_disciplina(
        id_disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        fk_id_professor INTEGER NOT NULL
    );
""")

print('tabela "tb_disciplina" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        fk_id_turno INTEGER NOT NULL
    );
""")

print('tabela "tb_curso" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_campus(
        id_campus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        sigla VARCHAR(3) NOT NULL,
        cidade VARCHAR(45) NOT NULL
    )
""")

print('tabela "tb_campus" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        fk_id_curso INTEGER NOT NULL
    );
""")

print('tabela "tb_turma" criada com sucesso!')

cursor.execute("""
    CREATE TABLE tb_turno(
        id_turno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(10) NOT NULL
    )
""")

print('tabela "tb_turno" criada com sucesso!')

conn.close()
