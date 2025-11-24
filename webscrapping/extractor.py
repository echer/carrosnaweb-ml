from bs4 import BeautifulSoup
import pandas as pd

def getManufacters(content):
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all(attrs={"action": "catalogo.asp"})[0].find_all('table')[1].find_all('a')

    ignorelinks = ['Página Principal', 'Todos']

    s1 = pd.Series([])

    for link in links:
        manufacter = link.contents[0].string
        href = link['href'].split('?')
        if(len(href) > 1 and manufacter not in ignorelinks):
            if(href[1].split('=')[0] == 'fabricante'):
                extract = href[1].split('=')[1]
                s1 = pd.concat([s1, pd.Series([extract])])
    return s1

def getModels(content):    
    s1 = pd.Series([])

    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('table')[2].find_all('a')
    
    ignorelinks = ['Página Principal', 'Todos', 'Catálogo']

    for link in links:
        model = link.contents[0].contents[0].string
        href = link['href'].split('?')

        if(len(href) > 1 and model not in ignorelinks):
            if(href[1].split('&')[1].split('=')[0] == 'modelo'):
                extract = href[1].split('&')[1].split('=')[1]
                s1 = pd.concat([s1, pd.Series([extract])])

    return s1