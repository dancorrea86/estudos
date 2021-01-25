from flaskModules import app

@app.route("/index")
@app.route("/")
def index():
    return "<h1>Ola</h1>"