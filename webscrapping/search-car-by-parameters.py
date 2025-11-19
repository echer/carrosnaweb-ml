import requests
from bs4 import BeautifulSoup
import pandas as pd

def getCar(manufacter, model, year):
    url = f'https://www.carrosnaweb.com.br/catalogo.asp?fabricante={manufacter}&varnome={model}&anoini={year}&anofim={year}'

    payload = {}
    headers = {
        #'Cookie': 'ASPSESSIONIDSWBQDCTC=FIGIGHLCMJNCOKNIOMAGPOIP'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    s1 = pd.Series([])

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all('table')[2].find_all('table')[0].find_all('a')
        
        ignorelinks = ['Página Principal', 'Catálogo', 'Todos']

        for link in links:
            href = link['href'].split('?')
            if(href[1].split('=')[0] == 'codigo'):
                extract = href[1].split('=')[1]
                s1 = pd.concat([s1, pd.Series([extract])])
                break
    return s1

#print(getCar('Changan','Avatr 11','2026'))