import pandas as pd

students = {
    "names" : ["ali" , 'ahmed' , "akber"],
    "age" : [11 ,22,21] ,
   "city" : ['karachi' , 'lahore' , "islamabad"],
   "marks" : [98 , 76 ,33]

}
df = pd.DataFrame(students)
print(df)
print(df.head()
)
print(df.tail()
)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df['names'])
print(df[['names','city']])
print(df.loc[2])
print(df.loc[1:3])
print(df.iloc[0:3, 1:3])
print(df[df["marks"]>85])
print(df[(df["marks"]>85) & (df["city"]=='karachi')])
print(df[(df['marks']>50) & (df['city']=='karachi') & (df['age']<20)])
print(df.sort_values('marks'))
print(df.sort_values('marks', ascending=False))
