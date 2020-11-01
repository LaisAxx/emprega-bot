from time import sleep
import telepot 

bot = telepot.Bot('')
idCanal = 

ler = open('vagas.json', 'r')
lerjson = json.loads(ler.read())
ler.close()

listaDeChaves = []
for i in range(len(lerjson)):
  chave = list(lerjson[i].keys())[0]
  listaDeChaves.append(chave)

for i in range(len(lerjson)):
  info = lerjson[i][listaDeChaves[i]]
  print(info)
  bot.sendMessage(idCanal, info, parse_mode="markdown")
  sleep(2)
print('vagas enviadas!')
