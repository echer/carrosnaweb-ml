import requests
from bs4 import BeautifulSoup
import pandas as pd

def getCarByManufacter(manufacter):
    url = f'https://www.carrosnaweb.com.br/catalogofabricante.asp?fabricante={manufacter}'

    payload = {}
    headers = {
        #'Cookie': 'ASPSESSIONIDSWBQDCTC=FIGIGHLCMJNCOKNIOMAGPOIP'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    s1 = pd.Series([])

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all('table')[2].find_all('a')
        
        ignorelinks = ['Página Principal', 'Todos', 'Catálogo']

        for link in links:
            model = link.contents[0].contents[0].string
            href = link['href'].split('?')

            if(len(href) > 1 and model not in ignorelinks):
                extract = href[1].split('=')[2]
                s1 = pd.concat([s1, pd.Series([extract])])

    return s1

#print(getCarByManufacter('Changan'))