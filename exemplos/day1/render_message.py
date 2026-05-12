from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


def addhearts(text):
    return f"❤️ {text} ❤️"

env.filters['addhearts'] = addhearts

template = env.get_template('email.template.txt')

data = {
    'name': 'Laercio',
    'products': [
        {'name': 'Notebook', 'price': 1000.215},
        {'name': 'Mouse', 'price': 100.509},
        {'name': 'Teclado', 'price': 200.756},
    ],
    'special_customer': True
}

print(template.render(**data))

