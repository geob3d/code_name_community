import json
import requests
from requests.auth import HTTPBasicAuth
from collections import defaultdict
import csv


#Authentication
USER = '85901'
PASS ='96d82728-6adb-4f63-bcb5-6ec9106d57c7'

#Base URL
baseurl = "https://api.ssactivewear.com"
# api-endpoint 
URL = { 
        "category":baseurl + "/v2/categories/?fields=CategoryID,Name",
        "style": baseurl + "/v2/styles/?fields=styleID,brandName,title,description,baseCategory,categories",
        "product": baseurl +  "/v2/products/81480,B00760004,00821780008137?fields=sku,styleID,colorName,sizeName,qty,brandName"
        }

#headers
headers = {"Accept":"applicaiton/json",
        "Content-type": "application/json"}




def ssProdCat(result):
        r = requests.get(url = URL["category"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

        # extracting data in json format 
        data = json.loads(r)

        #Result Dictionary
        result = {}


        for item in data:
                results=item["name"]
                result.append(results)
                print(result)


print(ssProdCat('result'))


#style
r = requests.get(url = URL["style"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

# extracting data in json format 
styleData = json.loads(r)

#category
s = requests.get(url = URL["category"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

# extracting data in json format 
cdata = json.loads(s)




#Result Dicionary
styleResult = []




for sitem in styleData:
        for citem in cdata:
                if str(citem["categoryID"]) in sitem["categories"].split(","):
                        
                        data={
                                "stylename":sitem["styleName"],
                                "brandname:": sitem['brandName'],
                                "oth" : [ ]


                                
                        }
                        yourlist=[]
                        yourlist.append(citem)

                        #data.update({'oth': citem["name"]})
                        #print(citem.get("name"))
                        #print(list(citem.values()))

                        #print(citem["name"])

                        #print(citem["name"])
                        #print(yourlist)
                
