# Scrape-Volantino-Project

Simple py scrape script that takes discounted product from DoveConviene flyers URLs stored in shops.txt and make JSON Data, stored in product.json, of every discounted product found in those flyers.
Run main.py and type what you wish to search, if discounted products with similar title or which contain the word inserted are found, those will be stored in offerte.json.

Offerte.json -> 
{
  "link": "URL" - DoveConviene.it URL to the discounted product
  "supermercato": "string" - Shop of the discounted product
  "prezzo": 0.0 - Price of the discounted product
}
