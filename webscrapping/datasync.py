import os
from downloader import *
from extractor import *

root_folder = 'local_cache'

def syncData():
    os.makedirs(root_folder, exist_ok=True)

    manufacters = processManufacters()
    for manufacter in manufacters:
        models = processModels(manufacter)
        for model in models:
            years = processYear(manufacter, model)
            for year in years:
                codes = processCode(manufacter, model, year)

def processManufacters():
    path = f'{root_folder}/manufacters'
    file = 'manufacter.html'
    full_path = f'{path}/{file}'

    if(not createExist(path, file)):
        return getManufacters(downloadManufacter(full_path))
    else:
        return getManufacters(readFile(full_path))
    
def processModels(manufacter):
    path = f'{root_folder}/{manufacter}'
    file = f'{manufacter}.html'
    full_path = f'{path}/{file}'
    if(not createExist(path, file)):
        return getModels(downloadModels(full_path, manufacter))
    else:
        return getModels(readFile(full_path))
    
def processYear(manufacter, model):
    path = f'{root_folder}/{manufacter}/{model}'
    file = f'{model}.html'
    full_path = f'{path}/{file}'
    if(not createExist(path, file)):
        return getYears(downloadYear(full_path, manufacter, model), manufacter)
    else:
        return getYears(readFile(full_path), manufacter)
    
def processCode(manufacter, model, year):
    path = f'{root_folder}/{manufacter}/{model}/{year}'
    file = f'{year}.html'
    full_path = f'{path}/{file}'
    if(not createExist(path, file)):
        return getCode(downloadCode(full_path, manufacter, model, year))
    else:
        return getCode(readFile(full_path))
        
def createExist(path, file):
    os.makedirs(path, exist_ok=True)
    return os.path.exists(f'{path}/{file}')

def readFile(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()