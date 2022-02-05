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
    product = input('Inserire prodotto, invia 0 per uscire: ')
    if(product == 0 or product == "0"): break
    
    saveProductAsJSON(ricercaProdotto(product))
    
    