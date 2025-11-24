
from bs4 import BeautifulSoup, Tag
import pandas as pd
from pathlib import Path

def getCarDetail(code):

    s1 = pd.Series([])

    with open(f"{code}.html", "r", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")
        tds = soup.find_all('table')[2].find_all('table')[0].find_all('td')

        ignoreidx = [0,1,2,3,4,5,6,7,8]
        ignoreattr = ['Nota do leitor']

        for idx, td in enumerate(tds):
            if(idx not in ignoreidx and type(td) is Tag):

                if(td.get('bgcolor') and td['bgcolor'] == '#ffffff' and td.get('colspan') is None):
                    for font in td.find_all('font'):
                        if(font.get('color') and font['color'] == 'darkred' and not font.string is None and font.string not in ignoreattr):
                            atributo = font.string
                            print('atributo:',atributo)
                            break

                if(not atributo is None and td.get('bgcolor') and td['bgcolor'] == '#efefef'):
                    fonts = td.find_all('font')
                    for font in fonts:
                        if (len(font.contents) == 1 and font.contents is not None):
                            valor = font.string
                            print('valor1:',valor)
                            atributo = None
                            break
                        elif (len(font.contents) > 1 and font.contents[0].string is not None):
                            valor = font.contents[0].string
                            print('valor2:',valor)  
                            atributo = None
                            break

                if(idx > 150):
                    break
                
                #print(fonts)
                #for font in fonts:
                #    if(type(font) is Tag and font.get('color') and font['color'] == 'darkred'):
                #        atributo = font.string
                #        print(atributo)
                #        continue

                 #   if(type(font) is Tag and font.parent.get('bgcolor') and font.parent['bgcolor'] == '#efefef'):
                #        valor = font.string
                #        print(valor)
                #        continue


                    

                #if(len(fonts) == 2):
                 #   print(fonts)

    #if(response.status_code == 200):
    #    soup = BeautifulSoup(response.text, "html.parser")
    #    links = soup.find_all('table')[2].find_all('table')[0].find_all('td')
    #    print(links)
        
    #    ignorelinks = ['Página Principal', 'Catálogo', 'Todos']

    #    for link in links:
    #        print(link)
    return s1

#getCarDetail('43585')