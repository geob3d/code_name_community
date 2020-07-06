
#consumer Key
#ck_d2d1609dedbf2d0c5e207737f83ed0a07b6f7ebf

#consumer secret
#cs_53b9fc8b6b30a856d0be92505078c56314b17c3f


from woocommerce import API
import json
import requests
from tycoapi import ssProdCat

wcapi = API(
    url="http://www.tycotees.com",
    consumer_key="ck_d2d1609dedbf2d0c5e207737f83ed0a07b6f7ebf",
    consumer_secret="cs_53b9fc8b6b30a856d0be92505078c56314b17c3f",
    version="wc/v3"
)



ssCat = str(ssProdCat('result'))

def wooCategories():

    for item in ssCat.split("\n"):
        data ={
            "name": item
            }
        #print(wcapi.post("products/categories", data).json())     
        print(data)
wooCategories()