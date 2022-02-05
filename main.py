from soupsieve import match
from funzioni import *
import json

shops = list()

with open('shops.txt', 'r') as f:
    for word in f:
        shops.append(word)

listaProdotti = dict()
cleanList = dict()

scrapeProducts(listaProdotti, cleanList, shops)
saveAsJSON(cleanList)

while(1):
    d = ricercaProdotto(input('Inserire prodotto: '))
    print(json.dumps(d, indent=2))