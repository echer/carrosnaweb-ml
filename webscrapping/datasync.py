import os
from downloader import *
from extractor import *

def syncData():

    root_folder = 'local_cache'

    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    html_manufacter_file = f'{root_folder}/manufacter.html'
    
    manufacters = getManufacters(createReadFile(html_manufacter_file, downloadManufacter(html_manufacter_file)))

    print(manufacters)

    for manufacter in manufacters:
        html_model_file = f'{root_folder}/{manufacter}.html'
        models = getModels(createReadFile(html_model_file, downloadModels(html_model_file, manufacter)))
        print(models)
        

    


def createReadFile(path, downloadf):
    if not os.path.exists(path):
        download = downloadf()
    else:
        with open(path, "r", encoding="utf-8") as f:
            download = f.read()
    return download