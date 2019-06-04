import sqlite3

conn = sqlite3.connect('EscolaServicoApp.db')

cursor = conn.cursor()


cursor.execute("""
    INSERT INTO tb_escola(nome, logradouro, cidade)
    VALUES(?,?,?);
""", ('IFPB - GUARABIRA','PB-057', 'Guarabira'))

print("Dados Escola inserida com sucesso!")

conn.close()
