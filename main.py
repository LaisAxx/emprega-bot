# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests 
import os.path
import utils 



# url 
url = ''

datas = []
titulos = [] 
links = [] 
descricoes = []
links = []

links_validos = utils.getLinksValidos(url, 60)
lista_soups = utils.getVagasValidas(links_validos)
datas = utils.getData(lista_soups)
titulos = utils.getTitulos(lista_soups)
descricoes = utils.getDescricao(lista_soups)
links = utils.getLinksValidos(url, 60)


listaDeVagas = []
for i in range(0,len(titulos)):
  vaga ={links_validos[i]:
   (titulos[i],datas[i], descricoes[i], links[i]) }
  listaDeVagas.append(vaga)
print(listaDeVagas)


listaChaves = [] # lista de tds as chaves do dic

nome_arquivo = 'vagas.json'


for i in range(len(listaDeVagas)):
  chaves = list(listaDeVagas[i].keys())[0] #pega as chaves do dicionario
  listaChaves.append(chaves) # add essas chaves em uma lista so de chaves 
#print(listaChaves)

if (os.path.exists(nome_arquivo)):
    arquivo_json = open(nome_arquivo,'r')
    #dados_json = json.loads(arquivo_json.read())
    dados_json = json.dumps(listaDeVagas, ensure_ascii=False, indent = 2)
    arquivo_json.close()  
else:
  dados_json = json.dumps(listaDeVagas, ensure_ascii=False, indent = 2)
  arquivo = open(nome_arquivo,'w')
  arquivo.write(dados_json)
  arquivo.close()

