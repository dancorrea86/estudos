from flask import Flask, request
import locale

from script import SimplesTaxCalculator

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    revenues_twelve_months = request.form['revenues-twelve-months'].replace('.','')
    revenue_month = request.form['revenue-month'].replace('.','')
    attachment = request.form['attachment']

    revenues_twelve_months = float(revenues_twelve_months.replace(',','.'))
    revenue_month = float(revenue_month.replace(',','.'))

    app = SimplesTaxCalculator(revenues_twelve_months, attachment, revenue_month)


    valor3 = locale.currency(valor3, grouping=True, symbol=None)
    # valor3 = '{:20,.2f}'.format(valor3)
    # valor3 = str(valor3)
    return (valor3)

if __name__ == '__main__':
    app.run(debug=True)