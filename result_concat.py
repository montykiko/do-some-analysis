import pandas as pd
from pandas import Series,DataFrame
import pymongo
import json

client = pymongo.MongoClient('localhost',27017)
kismet = client['kismet']
half_life = kismet['half_life']

df = pd.DataFrame(list(half_life.find()))
data = df.distribution.map(lambda x:isinstance(x,dict))
df = df.loc[data].copy()
emo1 = pd.DataFrame(df['distribution'].values.tolist())
emo2 = df[['polarity','magnitude','keywords']].copy()
emo3 = pd.concat([emo2,emo1],axis=1)
emo3 = emo3[1:].copy()
emo3.index = range(0,len(emo3))

df2 = pd.read_table('half_life.txt')
dff = pd.concat([df2,emo3],axis = 1)
dff.fillna(0,inplace = True)
dff.to_csv('half_life_result.csv',sep = ',',index = False,encoding = 'utf-8')

