from flask import Flask, request

app = Flask(__name__)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    valor = int(request.form['projectFilePath']) + 1 
    valor = str(valor)
    return (valor)

if __name__ == '__main__':
    app.run(debug=True)