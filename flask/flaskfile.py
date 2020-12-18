from flask import Flask, request
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    valor = request.form['projectFilePath'].replace('.','')
    valor2 = request.form['projectFilePath2'].replace('.','')

    valor = float(valor.replace(',','.'))
    valor2 = float(valor2.replace(',','.'))
    valor3 = (valor + valor2)

    valor3 = locale.currency(valor3, grouping=True, symbol=None)
    # valor3 = '{:20,.2f}'.format(valor3)
    # valor3 = str(valor3)
    return (valor3)

if __name__ == '__main__':
    app.run(debug=True)