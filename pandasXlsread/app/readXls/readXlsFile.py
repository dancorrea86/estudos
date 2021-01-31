import pandas as pd

def readXls(file):
    data = pd.read_excel(file)
    return (data)
