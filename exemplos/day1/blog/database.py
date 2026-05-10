from sqlite3 import connect

# 1 conectar com o banco de dados
conn = connect("blog.db")
cursor = conn.cursor()

# 2 definir e criar a tabela
cursor.execute("""\
    CREATE TABLE IF NOT EXISTS post (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR NOT NULL,
        content VARCHAR NOT NULL,
        author VARCHAR NOT NULL
    );
""")

# 3 - Criamos os posts iniciais para alimentar o banco de dados
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": "Python é eleita a linguagem mais popular por muitos desenvolvedores e pela revista tech masters.",
        "author": "Satoshi Namamoto"
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": "Neste tutorial você aprenderá como criar um blog utilizando Python.",
        "author": "Guido van Rossum"
    },
    {
        "title": "Python e Django",
        "content": "Python e Django são uma combinação poderosa para criar aplicações web.",
        "author": "Guido van Rossum"
    }
]

# 4 - Inserimos os posts caso o banco de dados esteja vazio
count = cursor.execute("SELECT * FROM post").fetchall()
if not count:
    cursor.executemany("""
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author)
    """, 
    posts)

    conn.commit()

# 5 - Verficamos que foi realmente inserido
posts_db = cursor.execute("SELECT * FROM post").fetchall()
assert len(posts_db) >= 2