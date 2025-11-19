import requests
from bs4 import BeautifulSoup
import pandas as pd

def getManufacters():

    url = "https://www.carrosnaweb.com.br/avancada.asp"

    payload = {}
    headers = {
        #'Cookie': 'ASPSESSIONIDSWBQDCTC=FIGIGHLCMJNCOKNIOMAGPOIP'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    s1 = pd.Series([], index=[])

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all(attrs={"action": "catalogo.asp"})[0].find_all('table')[1].find_all('a')

        ignorelinks = ['Página Principal', 'Todos']

        for link in links:
            manufacter = link.contents[0].string
            href = link['href']

            if(manufacter not in ignorelinks):
                s1 = pd.concat([s1, pd.Series([href], index=[manufacter])])
    return s1