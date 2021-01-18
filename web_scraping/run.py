import requests
from bs4 import BeautifulSoup as bs

URL = 'http://www8.receita.fazenda.gov.br/simplesnacional/aplicacoes.aspx?id=21'
page = requests.get(URL)

def get_login_token(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = [n['value'] for n in soup.find_all('input')
             if n['name'] == 'wpLoginToken']
    return token[0]
    
soup = bs(page.content, 'html.parser')
print(soup.prettify())