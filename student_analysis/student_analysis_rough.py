import numpy as np
import pandas as pd
import random

np.random.seed(42)

number=500
subject=3
st_id=np.arange(1,number+1)

math=np.random.randint(40,100,size=(number))
science=np.random.randint(40,100,size=(number))
english=np.random.randint(40,100,size=(number))

attendance=np.random.randint(60,100,size=(number))
dept=np.array(["CS","ISE","ECE","ME"])
some_dpt=np.random.choice(dept,size=(number))

data={
    "student id":st_id,
    "math":math,
    "science":science,
    "english":english,
    "attendance":attendance,
    "department":some_dpt
}

df=pd.DataFrame(data)
# print(df.head())
df["average"]=df[["math","science","english"]].mean(axis=1)
# print(df)
df["grade"] = np.where(df["average"] >= 85, "A",
               np.where(df["average"] >= 70, "B",
               np.where(df["average"] >= 55, "C", "D")))

# print(df)
top_students=df.sort_values(by="average",ascending=False)
# print(top_students.head())
# print(df[df["average"]>=50])
some=(df["average"]>=50).mean()
pass_rate=some*100
# print(pass_rate)
group=df.groupby("department")
# print(group["average"].mean())
math_mean=df["math"].mean()
math_std=df["math"].std()
df["math_zscore"]=(df["math"]-math_mean)/math_std
print(df.head())
some=df.to_csv("student_analysis.csv",index=False)