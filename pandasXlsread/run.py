import app
from app.readXls import readXlsFile

data = app.readXls.readXlsFile.readXls('Planilha Exemplo.xls')

for register in data.index:
    print(data['Nome'][register])