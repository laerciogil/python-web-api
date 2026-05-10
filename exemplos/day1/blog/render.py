from database import conn
from pathlib import Path

# 1 obter os dados
cursor = conn.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post").fetchall()
posts = [dict(zip(fields, result)) for result in results]

# 2 criar a pasta de destino do site
site_dir = Path("site")
site_dir.mkdir(exist_ok=True)

# 3 criar uma função para gerar a url com slug
def get_post_url(post):
    slug = post["title"].lower().replace(" ", "-")
    return f"{slug}.html"

# 4 renderizar a página index.html
index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li><a href='{get_post_url(post)}'>{post['title']}</a></li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)

# 5 renderizar as páginas individuais de cada post
post_template = Path("post.template.html").read_text()
for post in posts:
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(
        post_template.format(post=post)
    )

print("Site gerado com sucesso!")
conn.close()