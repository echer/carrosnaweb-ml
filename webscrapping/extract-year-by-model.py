import requests
from bs4 import BeautifulSoup
import pandas as pd

def getYearByModel(manufacter, model):
    url = f'https://www.carrosnaweb.com.br/catalogomodelo.asp?fabricante={manufacter}&modelo={model}'

    payload = {}
    headers = {
        #'Cookie': 'ASPSESSIONIDSWBQDCTC=FIGIGHLCMJNCOKNIOMAGPOIP'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    s1 = pd.Series([])

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all('table')[2].find_all('a')
        
        ignorelinks = ['Página Principal', 'Todos', 'Catálogo', manufacter]

        for link in links:
            year = link.contents[0].string
            href = link['href'].split('?')

            if(len(href) > 1 and year not in ignorelinks):
                print(href)
                if(href[1].split('&')[2].split('=')[0] == 'anoini'):
                    extract = href[1].split('&')[2].split('=')[1]
                    s1 = pd.concat([s1, pd.Series([extract])])

    return s1

print(getYearByModel('Changan','Avatr 11'))