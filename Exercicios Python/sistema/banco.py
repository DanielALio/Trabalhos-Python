import sqlite3 
# from janela import acervo

#Banco é um arquivo, ele é criado nessa linha caso não exista
conexao = sqlite3.connect("biblioteca.db")

#O cursor é o garçom, leva o comando até o banco e traz a resposta
cursor = conexao.cursor()

#Cria a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livro(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        titulo TEXT NOT NULL,
        autor TEXT,
        ano INTEGER
    )
""")

print("Tabela criada")

#Insere os livros
# for i in acervo:
#     cursor.execute(
#         "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
#         (i.titulo, i.autor, i.ano),
#     )

cursor.execute(
    "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
    ("Dom Casmurro", "Machado de Assis", 1899),
)

print("Inserido")
conexao.commit() #Envia os livros para o banco


cursor.execute("SELECT id, titulo, autor, ano FROM livro")

#O fetchall() puxa todas as linhas do select 
for codigo, titulo, autor, ano in cursor.fetchall():
    print(f"{codigo} - {titulo} - {autor} - {ano}")

conexao.close()
