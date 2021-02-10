import pandas as pd

listOfPayments = []

def faz():
    data = pd.read_excel(r'app/files/planilha.xlsx')

    # for itens in data:
    #     listOfPayments.append(pd.DataFrame(data, columns=['PA', 'Código', 'Valor']))

#format data portugues
#     data_em_texto = ‘{}/{}/{}’.format(data_atual.day, data_atual.month,
# data_atual.year)

    print(listOfPayments)

    for index, row in data.iterrows():
        listOfPayments.append((row['Vencimento'], row['Recolhimento']))

    print (listOfPayments)