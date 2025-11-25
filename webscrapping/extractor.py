from bs4 import BeautifulSoup
import pandas as pd

def getManufacters(content):
    s1 = pd.Series([])

    if(content is None):
        return s1
    
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all(attrs={"action": "catalogo.asp"})[0].find_all('table')[1].find_all('a')

    ignorelinks = ['Página Principal', 'Todos']

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

    if(content is None):
        return s1

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

def getYears(content, manufacter):
    s1 = pd.Series([])

    if(content is None):
        return s1

    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('table')[2].find_all('a')
    
    ignorelinks = ['Página Principal', 'Todos', 'Catálogo', manufacter]

    for link in links:
        year = link.contents[0].string
        href = link['href'].split('?')

        if(len(href) > 1 and year not in ignorelinks):
            if(href[1].split('&')[2].split('=')[0] == 'anoini'):
                extract = href[1].split('&')[2].split('=')[1]
                s1 = pd.concat([s1, pd.Series([extract])])
    return s1

def getCode(content):
    s1 = pd.Series([])

    if(content is None):
        return s1
    
    print(content)

    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('table')[2].find_all('table')[0].find_all('a')

    for link in links:
        href = link['href'].split('?')
        if(href[1].split('=')[0] == 'codigo'):
            extract = href[1].split('=')[1]
            s1 = pd.concat([s1, pd.Series([extract])])
            break
    return s1