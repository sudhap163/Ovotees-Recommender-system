import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.ovotees

catalog_price = []
catalog_discount = []
catalog_type = []
catalog_sleeves = []
catalog_fabric = []
catalog_color = []
catalog_size = []

catalog = db.catalog

for item in catalog.find():
    for color in item['color']:
        for size in item['size']:
            catalog_price.append(item['price'])
            catalog_discount.append(item['discount'])
            catalog_type.append(item['type'])
            catalog_sleeves.append(item['sleeves'])
            catalog_fabric.append(item['fabric'])
            catalog_color.append(color)
            catalog_size.append(size)

catalog_type = pd.get_dummies(catalog_type)
catalog_sleeves = pd.get_dummies(catalog_sleeves)
catalog_fabric = pd.get_dummies(catalog_fabric)
catalog_color = pd.get_dummies(catalog_color)
catalog_size = pd.get_dummies(catalog_size)
print(catalog_size)