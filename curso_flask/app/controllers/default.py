from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hellor world!"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s" % name
    else:
        return "Olá, usuário"

# @app.route("/test", defaults={'id': 0})
# @app.route("/test/<int:id>")
# def test(id):
#     if id:
#         return str(id)
#     else:
#         return "Não encontrado"