from soupsieve import match
from funzioni import *
import re

shops = list()

with open('shops.txt', 'r') as f:
    for word in f:
        shops.append(word)

listaProdotti = dict()
cleanList = dict()

scrapeProducts(listaProdotti, cleanList, shops)
saveAsJSON(cleanList)
d = ricercaProdotto(input('Inserire prodotto: '))
print(d)
