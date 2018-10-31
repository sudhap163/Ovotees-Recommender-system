# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:31:12 2018

@author: Sudha
"""

import math
import numpy as np
import pandas as pd
from pymongo import MongoClient
#from sklearn.neighbors import KNeighborsClassifier

client = MongoClient('mongodb://fastechfashions.com', 25378)
db = client.ovotees

catalog_price = []
catalog_discount = []
catalog_type = []
catalog_sleeves = []
catalog_fabric = []
data = []

catalog = db.catalog

for item in catalog.find():
    
    catalog_price.append(item['price'])
    if (math.isnan(float(item['discount']))):
        catalog_discount.append(0)
    else:
        catalog_discount.append(item['discount'])
    catalog_type.append(item['type'])
    catalog_sleeves.append(item['sleeves'])
    catalog_fabric.append(item['fabric'])

catalog_price = np.array(catalog_price)
catalog_discount = np.array(catalog_discount)
catalog_type = np.array(pd.get_dummies(catalog_type))
catalog_sleeves = np.array(pd.get_dummies(catalog_sleeves))
catalog_fabric = np.array(pd.get_dummies(catalog_fabric))

data.append(catalog_price)
data.append(catalog_discount)
print(np.array(data).shape, np.array(data).size)
print("\n\n\n\n\n\n\n\n")
for x in catalog_type:
    print(x)
    print("\n")
    data.append(x.T)
print(data)
print(np.array(data).shape, np.array(data).size)
print("\n\n\n\n\n\n\n\n")
for x in catalog_sleeves:
    data.append(x)
for x in catalog_fabric:
    data.append(x)

data = np.array(data)
    
#print(data.shape)

#print(neigh.predict([['135', '0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '0.0', '1.0', '1.0', '0.0','0.0', '0.0']]))
#print(neigh.predict_proba([['135', '0', '0.0', '1.0', '0.0', '0.0', '0.0', '0.0', '0.0', '1.0', '1.0', '0.0','0.0', '0.0']]))