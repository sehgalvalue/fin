import pandas as pd
import glob
from os import walk
equity = pd.read_csv('/Users/staff/Desktop/RahulCode/remaining-companies.csv')
equity.columns =['Company Registered Number']
equity['Company Registered Number']=equity['Company Registered Number'].astype('str')
equity["num"]= equity["Company Registered Number"].str.pad(8, side ='left', fillchar ='0')
data_list = list(set(equity['num']))
data2 = pd.DataFrame(data_list)
data2.columns = ['num']
import pandas as pd
import zipfile
a=[]
mypath ='/Users/staff/Desktop/RahulCode/Data'
f = []
file_names=[]
for(dirpath, dirnames, filenames) in walk(mypath):
    for names in filenames:
        file_names.append(names)
        filepath=mypath+'/'+names
        with zipfile.ZipFile(filepath,'r') as g:
            for name in g.namelist():
                f.append(filepath+'/'+name)
                
                
headers = [tuple(i.split('_')) for i in f]
data1 = [x[4] for x in headers]
df_work = pd.DataFrame(f, columns=['Names'])
df_work['Nums']=data1
b=data2['num']

final=df_work.merge(data2, how='inner', left_on='Nums', right_on='num')

a=final['Names'].values.tolist()
final.to_csv('/Users/staff/Desktop/finalpyfile.csv')