import numpy as np
import pandas as pd

df=pd.read_csv("superstore.csv",encoding="latin1")
# print(df.shape)
# print(df.info())
# print(df["Sales"].sum())
# print(df["Profit"].sum())
# print(df.sort_values(by="Region").head())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df["Sales"].mean())
# print(df["Profit"].mean())
# print(df.sort_values(by="region"))
# group=df.groupby(by="Region")
# some=group["Sales"].sum()
# print(some.sort_values(ascending=False))
# # print(group["Sales"].sum())
# group=df.groupby(by="Region")
# some=group["Profit"].sum()
# print(some.sort_values(ascending=False))

# group=df.groupby(by="Sub-Category")
# some=group["Sales"].sum()
# print(some.sort_values(ascending=False))
# group=df.groupby(by="Sub-Category")
# some=group["Profit"].sum()
# print(some.sort_values(ascending=False))

array=np.array(df["Sales"])
# print(array)
# # m=np.sum(array)
# print(np.mean(array))
# print(np.sum(array))
# print(np.std(array))
# print(np.median(array))
# top_sales=df.sort_values(by="Sales")
# print(top_sales.head)
# group=df.groupby(by="Product Name")
# some=group["Sales"].sum()
# print(some.sort_values(ascending=False).head())
minimum=np.min(array)
maximum=np.max(array)
norm=(array-minimum)/(maximum-minimum)
# print(norm)
sale_mean=np.mean(array)
sale_std=np.std(array)
zscore=(array-sale_mean)/sale_std
print(zscore)
out=abs(zscore)
count=0
for i in out:
    if i>3:
        count=count+1
        
print(count)