import sqlite3 
# from janela import acervo

#Banco é um arquivo, ele é criado nessa linha caso não exista
conexao = sqlite3.connect("biblioteca.db")

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


cursor.execute(
    "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
    ("O nome do vento", "Patrick Rothfuss", 2009),
)

print("Inserido")
conexao.commit() #Envia os livros para o banco


cursor.execute("SELECT id, titulo, autor, ano FROM livro")

for codigo, titulo, autor, ano in cursor.fetchall():
    print(f"{codigo} - {titulo} - {autor} - {ano}")

conexao.close()
