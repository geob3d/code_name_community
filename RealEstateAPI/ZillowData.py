import pandas as pd 
import csv

df = pd.read_csv('SaleToListRatio_City.csv', sep=',')





df2 = pd.melt(df, id_vars=['SizeRank','RegionID','RegionName','RegionType','StateName'], 
                  var_name="Date", value_name="Value")

#datahead = df.head()
#print(datahead)

print(df2)

df2.to_csv('file_name.csv', sep=',')                                                     

print('complete')