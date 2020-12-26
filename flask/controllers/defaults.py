from ../ import app

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "hello"

@app.route('/user/<username>')
def user(username):
    return "Olá %s" %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    return 'ok'