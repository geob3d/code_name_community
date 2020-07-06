import json
import requests
from requests.auth import HTTPBasicAuth
from collections import defaultdict
import pymysql
pymysql.install_as_MySQLdb()

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


#Mysql Conneciton
con = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = 'C@mera12',db = 'TycoTees', port=3306, autocommit = True)
Cursor = con.cursor()


def ssProdCat():
        r = requests.get(url = URL["category"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

        # extracting data in json format 
        data = json.loads(r)

        #Result Dictionary
        #result = []


        for item in data:
                #results=item["name"]
                #result.append(item)
        #return  result
                catid = item.get('categoryID')
                cat_name = item.get("name")
                #print(catid +" "+ cat_name)
                
                Cursor.execute("INSERT INTO Categories (categoryID,  catname) VALUES (%s, %s)", (catid,cat_name))



def ssStyles():
        r = requests.get(url = URL["style"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

        # extracting data in json format 
        data = json.loads(r)

        for item in data:
                styleID = item.get("styleID")
                brandName = item.get("brandName")
                title = item.get("title")
                description = item.get("description")
                baseCategory = item.get("baseCategory")
                categories = item.get("categories")
                print(styleID)


                Cursor.execute("INSERT INTO Styles(styleID,brandName,title,descriptions,baseCategory,categories) VALUES (%s,%s,%s,%s,%s,%s)", (styleID,brandName,title,description,baseCategory,categories))




ssStyles()