from typing import final
import requests
import json
import csv
import re
from csv import writer
from bs4 import BeautifulSoup

def scrapeProducts(raw_dict, clean_dict, shops):
    for shop in shops:
        r = requests.get(shop)

        soup = BeautifulSoup(r.content, 'html.parser')
        res = soup.find_all('script', type = 'application/ld+json')[3:]

        for item in res:
            CT = item.contents[0]
            newItem = json.loads(CT)
            # Prende dalla entry del prodotto i campi image (link all'immagine dell'offerta) e offers (dati dell'offerta)
            raw_dict[newItem['name']] = {
                key: newItem[key] for key in newItem.keys() & ({'image'} | {'offers'})
            }


        for k,v in raw_dict.items():
            # print(k,v)
            clean_dict[k] = {'prezzo': v['offers']['price'], 'supermercato': v['offers']['seller']['name'], 'link': v['image'][0]}

def saveAsCSV(product_dict):
    from csv import writer
    with open('offerte.csv', 'a') as f_object:

        writer_object = writer(f_object)

        fieldnames = ['prodotto', 'prezzo', 'supermercato']
        writer = csv.DictWriter(f_object, fieldnames=fieldnames)

        for k,v in product_dict.items():
            writer.writerow({'prodotto': k, 'prezzo': v['prezzo'], 'supermercato': v['supermercato']})

        f_object.close()

def saveAsJSON(product_dict):
    with open('offerte.json', 'w') as f:
        json.dump(product_dict, f)

        f.close()

def ricercaProdotto(product):

    matched_dict = dict()

    with open('offerte.json','r') as f:
        prod_dict = json.load(f)

        for k,v in prod_dict.items():
            # print(product, k, v)
            if re.search(product, k, re.IGNORECASE):
                matched_dict[k] = v

        f.close()

    return matched_dict

def saveProductAsJSON(product):
    with open('products.json', 'w') as f:
        json.dump(product, f, indent=2)

        f.close()