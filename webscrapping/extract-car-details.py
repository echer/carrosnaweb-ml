import requests
from bs4 import BeautifulSoup, Tag
import pandas as pd
from pathlib import Path

def getCarDetail(code):
    url = f'https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo={code}'

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        #'Cookie': '_ga=GA1.1.1597651777.1763554871; clever-counter-60467=0-1; _cc_id=5d79de02092a8c8d935b728032b7cdfd; panoramaId_expiry=1763641293550; panoramaId=53c4c004f5152c6f9c5444bebf1ca9fb927af5eaaa03b957b7e9d3df1d56df76; panoramaIdType=panoDevice; cto_bundle=PqD5s181T2hybkU5SW8lMkJDZWU0dzNWNFdBJTJCM1RWMGglMkI0ekJoS2I3VWdlcGkwdEp5RlI3dVh1NmFXenNudG45YTdNSmN5ZmNJb3AwMWJobWRaQ2NERXY0UW8xT0F2dU1BaEF2YkNBVjZ0TWx4UGt5WVFsa0dqU2ZMWDliJTJCSW00d0QlMkZLcm90bnQzTjNVVkpFOEJrMXprYU9zWGVFUzM2ZENWWmhOTUNZdWR1Sjd4RW5rJTNE; cto_bundle=PqD5s181T2hybkU5SW8lMkJDZWU0dzNWNFdBJTJCM1RWMGglMkI0ekJoS2I3VWdlcGkwdEp5RlI3dVh1NmFXenNudG45YTdNSmN5ZmNJb3AwMWJobWRaQ2NERXY0UW8xT0F2dU1BaEF2YkNBVjZ0TWx4UGt5WVFsa0dqU2ZMWDliJTJCSW00d0QlMkZLcm90bnQzTjNVVkpFOEJrMXprYU9zWGVFUzM2ZENWWmhOTUNZdWR1Sjd4RW5rJTNE; cto_bidid=jMwmbl9ObUwxZGdqOU01SW1DOUlzNGtvWENpVFB2dnh0UnhGc01vRUFVQ0tIM1ZodnhxS2ZOODl4NmNYRUtTJTJGQkc0TzZSY2YxVmdsUDMlMkZKZnk0aG52djVCMjB6TXViMHlYRnRNUVdmMlpqTmV1MVB6ME1SV3VHR0RWVGpHclp1UThsZ3g; ASPSESSIONIDSWBQDCTC=OPGLKHLCLBNMJHMDAPKJPKEA; __gads=ID=9b7858cbf7094d65:T=1763554871:RT=1763593505:S=ALNI_MZqAdoVY4RkG9imJMlJBkarPctUGQ; __gpi=UID=000012a7d8bbc1b8:T=1763554871:RT=1763593505:S=ALNI_Mbs8QMNqbFqgk-QrigMtQsUUMxhhw; __eoi=ID=ce814db8610514cd:T=1763554871:RT=1763593505:S=AA-AfjYwKKyw-2s5G9Mz0aLmrbvH; ASPYRWCTLECXDYCNQW=5; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22d58f8dd0-893a-45fb-a19b-8340e3a5491d%5C%22%2C%5B1763554872%2C962000000%5D%5D%22%5D%5D%5D; _ga_ZJLSJKVTQG=GS2.1.s1763592807$o4$g1$t1763593658$j41$l0$h0; FCNEC=%5B%5B%22AKsRol_5yKEGYI_0GzNJwG9tlSwtbHUmP2sMcC4PWQgC7QA05NRNPQLV9FSkj6LQsZVbIcLZDP1nLhgcJk3uMjuGXme8igtt5Pgf7Ss_E60BXTlBu2ZzCQqALBfIUExBULVdrPaj7WT00kwDAvgYShUlPBR2qD3A2A%3D%3D%22%5D%5D; ASPSESSIONIDSWBQDCTC=EDGMKHLCEJJMDNIGHIMPEODG; ASPYRWCTLECXDYCNQW=6'
    }

    #response = requests.request("GET", url, headers=headers, data=payload)

    s1 = pd.Series([])

    with open("detalhe.html", "r", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")
        tds = soup.find_all('table')[2].find_all('table')[0].find_all('td')

        ignoreidx = [0,1,2,3,4,5,6,7,8]

        for idx, td in enumerate(tds):
            #print(idx)
            if(idx not in ignoreidx and type(td) is Tag):

                #print(td)

                if(td.get('bgcolor') and td['bgcolor'] == '#ffffff'):
                    for font in td.find_all('font'):
                        if(font.get('color') and font['color'] == 'darkred'):
                            print('atributo:',font.string)

                if(td.get('bgcolor') and td['bgcolor'] == '#efefef'):
                    for font in td.find_all('font'):
                        if (len(font.contents) == 1 and font.string is not None):
                            print('valor1:',font.string)
                        elif (len(font.contents) > 1 and font.contents[0].string is not None):
                            print('valor2:',font.contents[0].string)
                        #else:
                        #    ahrefs = font.find_all('a') 
                        #    if len(ahrefs) > 0:
                        #        print('valor3:',ahrefs[0].string)
                                

                if(idx > 30):
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

getCarDetail('43585')