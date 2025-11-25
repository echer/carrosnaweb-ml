import requests

def downloadManufacter(path):
    url = "https://www.carrosnaweb.com.br/avancada.asp"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code == 200 and "Ocorreu um erro." not in response.text):
        with open(path, 'w', encoding="utf-8") as file:
            file.write(response.text)
        print(f'SUCCESS page: manufacters')
        return response.text
    else:
        print(f'=> ERROR page: manufacters - {url}')
        return None

def downloadModels(path, manufacter):
    url = f'https://www.carrosnaweb.com.br/catalogofabricante.asp?fabricante={manufacter}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code == 200 and "Ocorreu um erro." not in response.text):
        with open(path, 'w', encoding="utf-8") as file:
            file.write(response.text)
        print(f'SUCCESS page: {manufacter}')
        return response.text
    else:
        print(f'=> ERROR page: {manufacter} - {url}')
        return None

def downloadYear(path, manufacter, model):
    url = f'https://www.carrosnaweb.com.br/catalogomodelo.asp?fabricante={manufacter}&modelo={model}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code == 200 and "Ocorreu um erro." not in response.text):
        with open(path, 'w', encoding="utf-8") as file:
            file.write(response.text)
        print(f'SUCCESS page: {manufacter} - {model}')
        return response.text
    else:
        print(f'=> ERROR page: {manufacter} - {model} - {url}')
        return None

def downloadCode(path, manufacter, model, year):
    url = f'https://www.carrosnaweb.com.br/catalogo.asp?fabricante={manufacter}&varnome={model}&anoini={year}&anofim={year}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code == 200 and "Ocorreu um erro." not in response.text):
        with open(path, 'w', encoding="utf-8") as file:
            file.write(response.text)
        print(f'SUCCESS page: {manufacter} - {model} - {year}')
        return response.text
    else:
        print(f'=> ERROR page: {manufacter} - {model} - {year} - {url}')
        return None

def downloadCarDetails(code):
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

    response = requests.request("GET", url, headers=headers, data=payload)

    if(response.status_code == 200 and "Ocorreu um erro." not in response.text):
        print(f'SUCCESS page: {code}')
        return response.text
    else:
        print(f'=> ERROR page: {code} - {url}')
        return None


