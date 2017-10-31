import pandas as pv

df = pv.read_csv("en_train.csv")
print(df[df['before']==df['after']].groupby(by="class").count())
# print(df.columns)
