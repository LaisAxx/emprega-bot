import time
from datetime import date, timedelta

# Recupera todas as urls válidas respeitando o limite de dias
# e já navegando para as outras páginas
def getLinksValidos(url, dias):
  cont = 1
  urls_validas, flag_proxima_pag = vagasValidas(url, dias)
  while flag_proxima_pag:
    cont += 1
    url2 = f'{url}page/{cont}/'
    urls_validas2, flag_proxima_pag = vagasValidas(url2, dias)
    urls_validas += urls_validas2
  return urls_validas

# Função auxiliar
def vagasValidas(url, dias):
  site = requests.get(url)
  soup = BeautifulSoup(site.content, 'html.parser')
  urls_validas = []
  flag_proxima_pag = True
  for item in soup.select('article'): #pega o article
    item2 = item.find_all('span', class_="thetime")[0]
    data_vaga = item2.get_text()
    if confereData(data_vaga, dias):
      urls_validas.append(item.a.get('href'))
    else:
      # Se for falso para essa flag, quer dizer que não é necessário ir para a
      # próxima página
      flag_proxima_pag = False
  return urls_validas, flag_proxima_pag

# Função auxiliar
# Recebe a data da vaga(dia/mes/ano) como string e dias significa quantidade de dias a serem considerados para tras 
def confereData(data_vaga, dias):
  dia, mes, ano = map(int, data_vaga.split('/'))
  data_vaga = date(ano, mes, dia)
  data_limite = date.today() - timedelta(days=dias)
  return data_vaga >= data_limite

# Função que retorna uma lista de soups referente a lista de links válidos
def getVagasValidas(links_validos):
  lista_soup = []
  for url in links_validos:    
    site = requests.get(url)
    soupVaga = BeautifulSoup(site.content, 'html.parser')
    lista_soup.append(soupVaga)
    time.sleep(5)
  return lista_soup

# Recebe uma lista de soups (páginas válidas) e devolve uma lista de descrições
# na mesma ordem.
def getDescricao(lista_soups):
  lista_descricao = []
  for soupVaga in lista_soups:
    desc_vaga_soup = soupVaga.find_all('div', class_="m_-6996655759212691418gmail-m_-8205393197000569422gmail-font8")[1]
    desc_vaga_soup = desc_vaga_soup.div
    desc_vaga = []
    for p in desc_vaga_soup.find_all(['p','ul']):
      desc_vaga.append(p.get_text())

    desc_vaga_limpo = [' '.join(t.split()) for t in desc_vaga]
    lista_descricao.append(desc_vaga_limpo)
  return lista_descricao

#puxa os links dos titulos
# def getLinks(lista_soups):
#   links = []
#   for soupVaga in lista_soups:
#     for item in soupVaga.select('article'):
#       for item2 in  item.find_all('header'):
#         for item3 in item2.find_all('a'):
#           if (item3.get('href').find('author/administrador') == -1):
#             links.append(item3.get('href'))
#     #print(links)
#   return links

#PEGA AS DATAS ok
def getData(lista_soups):
  datas = []
  for soupVaga in lista_soups:
    for item in soupVaga.select('article'): #pega o article
      for item2 in item.find_all('span', class_="thetime"):
        datas.append(item2.get_text())
    #print(datas)
  return datas

# puxa os titulos
def getTitulos(lista_soups):
  titulos = []
  for soupVaga in lista_soups:
    for item in soupVaga.find_all('article'):  
      for item2 in item.find_all(class_="title"):
        titulos.append(item2.get_text())
  return titulos  






import time
from datetime import date, timedelta

# Recupera todas as urls válidas respeitando o limite de dias
# e já navegando para as outras páginas
def getLinksValidos(url, dias):
  cont = 1
  urls_validas, flag_proxima_pag = vagasValidas(url, dias)
  while flag_proxima_pag:
    cont += 1
    url2 = f'{url}page/{cont}/'
    urls_validas2, flag_proxima_pag = vagasValidas(url2, dias)
    urls_validas += urls_validas2
  return urls_validas

# Função auxiliar
def vagasValidas(url, dias):
  site = requests.get(url)
  soup = BeautifulSoup(site.content, 'html.parser')
  urls_validas = []
  flag_proxima_pag = True
  for item in soup.select('article'): #pega o article
    item2 = item.find_all('span', class_="thetime")[0]
    data_vaga = item2.get_text()
    if confereData(data_vaga, dias):
      urls_validas.append(item.a.get('href'))
    else:
      # Se for falso para essa flag, quer dizer que não é necessário ir para a
      # próxima página
      flag_proxima_pag = False
  return urls_validas, flag_proxima_pag

# Função auxiliar
# Recebe a data da vaga(dia/mes/ano) como string e dias significa quantidade de dias a serem considerados para tras 
def confereData(data_vaga, dias):
  dia, mes, ano = map(int, data_vaga.split('/'))
  data_vaga = date(ano, mes, dia)
  data_limite = date.today() - timedelta(days=dias)
  return data_vaga >= data_limite

# Função que retorna uma lista de soups referente a lista de links válidos
def getVagasValidas(links_validos):
  lista_soup = []
  for url in links_validos:    
    site = requests.get(url)
    soupVaga = BeautifulSoup(site.content, 'html.parser')
    lista_soup.append(soupVaga)
    time.sleep(5)
  return lista_soup

# Recebe uma lista de soups (páginas válidas) e devolve uma lista de descrições
# na mesma ordem.
def getDescricao(lista_soups):
  lista_descricao = []
  for soupVaga in lista_soups:
    desc_vaga_soup = soupVaga.find_all('div', class_="m_-6996655759212691418gmail-m_-8205393197000569422gmail-font8")[1]
    desc_vaga_soup = desc_vaga_soup.div
    desc_vaga = []
    for p in desc_vaga_soup.find_all(['p','ul']):
      desc_vaga.append(p.get_text())

    desc_vaga_limpo = [' '.join(t.split()) for t in desc_vaga]
    lista_descricao.append(desc_vaga_limpo)
  return lista_descricao

#puxa os links dos titulos
# def getLinks(lista_soups):
#   links = []
#   for soupVaga in lista_soups:
#     for item in soupVaga.select('article'):
#       for item2 in  item.find_all('header'):
#         for item3 in item2.find_all('a'):
#           if (item3.get('href').find('author/administrador') == -1):
#             links.append(item3.get('href'))
#     #print(links)
#   return links

#PEGA AS DATAS ok
def getData(lista_soups):
  datas = []
  for soupVaga in lista_soups:
    for item in soupVaga.select('article'): #pega o article
      for item2 in item.find_all('span', class_="thetime"):
        datas.append(item2.get_text())
    #print(datas)
  return datas

# puxa os titulos
def getTitulos(lista_soups):
  titulos = []
  for soupVaga in lista_soups:
    for item in soupVaga.find_all('article'):  
      for item2 in item.find_all(class_="title"):
        titulos.append(item2.get_text())
  return titulos  






