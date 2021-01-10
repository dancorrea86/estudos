from app import app


@app.route("/")
def index():
    return "Hellor world!"

@app.route("/home")
def home():
    return "Home"