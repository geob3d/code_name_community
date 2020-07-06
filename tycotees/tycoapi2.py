import json
import requests
from requests.auth import HTTPBasicAuth
from collections import defaultdict
import pandas as pd
from itertools import chain
import numpy as np
import xlwt
import openpyxl


#Authentication
USER = '85901'
PASS ='96d82728-6adb-4f63-bcb5-6ec9106d57c7'

#Base URL
baseurl = "https://api.ssactivewear.com"
# api-endpoint 
URL = { 
        "category":baseurl + "/v2/categories/?fields=CategoryID,Name",
        "style": baseurl + "/v2/styles/?fields=styleID,brandName,title,description,baseCategory,categories,comparableGroup,styleImage",
        "product": baseurl +  "/v2/products/?fields=sku,styleID,styleName,colorName,sizeName,qty,brandName,color1,color2"
        }

#headers
headers = {"Accept":"applicaiton/json",
        "Content-type": "application/json"}




def ssProdCat():
        r = requests.get(url = URL["category"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

        # extracting data in json format 
        data = json.loads(r)

        #Result Dictionary
        #Sresult = {}


        #for item in data:
                #results=item["name"]
                #print(results)

        df = pd.read_json(r, orient='columns')
        print(df.head(10))


def ssProdStyle():
        r = requests.get(url = URL["style"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text
        s = requests.get(url = URL["category"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text
        t = requests.get(url = URL["product"],  auth=HTTPBasicAuth(USER,PASS), headers=headers).text

        # extracting data in json format 
        data = json.loads(r)
        data2 = json.loads(s)

        #Result Dictionary
        #Sresult = {}


        #for item in data:
                #results=item["name"]
                #print(results)

        #Setting up Styles Data Frame
        df = pd.read_json(r, orient='columns')
        s1 = df.categories.str.split(',', expand=True).stack().str.strip().reset_index(level=1, drop=True)
        df1 = pd.concat([s1], axis=1, keys=['categories'])
        z = df.drop(['categories'], axis=1).join(df1).reset_index(drop=True)


        #setting up Categories Data Frame
        df3 = pd.read_json(s, orient='columns') # Categories Df

        #Merge Styles and Categories
        df4 = z.merge(df3, left_on = z['categories'].astype(str),right_on =df3['categoryID'].astype(str))

        # Merge Styles/Categories DF with Products
        df5 = pd.read_json(t, orient='columns')


        df6 = pd.merge(df5,df4,on='styleID',how='left')
        #df6 =  df5.merge(df4, left_on = df5['styleID'],right_on =df4['styleID'])
        #df7 = df6.reset_index(drop=True)


        df6.to_excel('testfile.xlsx', index=False)

        




        return df6
        

        print("complete")

print(ssProdStyle())