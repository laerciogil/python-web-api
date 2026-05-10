# callable - function(..), obj(..), (lambda)(..)
# environ, callback (start_response)
# return iterable

def application(environ, start_response):
    # faz o que quiser com o request
    print(environ)

    # monta a response
    status = "200 OK"
    headers = [('Content-Type', 'text/html')]
    body = b'<strong>Hello World!!!</strong>'
    start_response(status, headers)
    return [body]

# if __name__ == '__main__':
#     from wsgiref.simple_server import make_server
#     server = make_server('0.0.0.0', 8000, application)
#     server.serve_forever()