# carregar os dados
dados = [
    {"nome": "Laercio", "cidade": "Fortaleza"},
    {"nome": "Joao", "cidade": "Sao Paulo"},
    {"nome": "Maria", "cidade": "Rio de Janeiro"},
]

# processsar
template = """
<html>
    <body>
        <ul>
            <li>Nome: {dados[nome]}</li>
            <li>Cidade: {dados[cidade]}</li>
        </ul>
    </body>
</html>
"""

# renderizar
for item in dados:
    print(template.format(dados=item))