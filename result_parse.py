import pandas as pd
import os


files = os.listdir('results')
colum_list = ['domain_cond','lm','tok_mean','pmi','dcpmi']
few_shot = ['0-shot','1-shot','2-shot','5-shot','10-shot']
wic = {element:{} for element in few_shot}
wsc = {element:{} for element in few_shot}
sst = {element:{} for element in few_shot}
agn = {element:{} for element in few_shot}
for colum in colum_list:
    for key in wic.keys():
        wic[key][colum] = 0
        wsc[key][colum] = 0
        sst[key][colum] = 0
        agn[key][colum] = 0
for file in files:
    with open('results/'+file) as f:
        content = f.readlines()
        for line in content:
            line = line.strip()
            if len(line)>5:
                for index,element in enumerate(line.split('&')):
                    element = element.strip()
                    element = float(element)
                    if 'wic' in file:
                        if '1-shot' in file:
                            wic['1-shot'][colum_list[index]] += element/3
                        elif '2-shot' in file:
                            wic['2-shot'][colum_list[index]] += element/3
                        elif '5-shot' in file:
                            wic['5-shot'][colum_list[index]] += element/3
                        elif '10-shot' in file:
                            wic['10-shot'][colum_list[index]] += element/3
                        else:
                            wic['0-shot'][colum_list[index]] += element/3
                    elif 'wsc' in file:
                        if '1-shot' in file:
                            wsc['1-shot'][colum_list[index]] += element/3
                        elif '2-shot' in file:
                            wsc['2-shot'][colum_list[index]] += element/3
                        elif '5-shot' in file:
                            wsc['5-shot'][colum_list[index]] += element/3
                        elif '10-shot' in file:
                            wsc['10-shot'][colum_list[index]] += element/3
                        else:
                            wsc['0-shot'][colum_list[index]] += element/3
                    elif 'sst' in file:
                        if '1-shot' in file:
                            sst['1-shot'][colum_list[index]] += element/3
                        elif '2-shot' in file:
                            sst['2-shot'][colum_list[index]] += element/3
                        elif '5-shot' in file:
                            sst['5-shot'][colum_list[index]] += element/3
                        elif '10-shot' in file:
                            sst['10-shot'][colum_list[index]] += element/3
                        else:
                            sst['0-shot'][colum_list[index]] += element/3
                    elif 'agn' in file:
                        if '1-shot' in file:
                            agn['1-shot'][colum_list[index]] += element/3
                        elif '2-shot' in file:
                            agn['2-shot'][colum_list[index]] += element/3
                        elif '5-shot' in file:
                            agn['5-shot'][colum_list[index]] += element/3
                        elif '10-shot' in file:
                            agn['10-shot'][colum_list[index]] += element/3
                        else:
                            agn['0-shot'][colum_list[index]] += element/3
df1 = pd.DataFrame.from_dict(wic)
df2 = pd.DataFrame.from_dict(wsc)
df3 = pd.DataFrame.from_dict(sst)
df4 = pd.DataFrame.from_dict(agn)
df1.to_csv('wic.csv')
df2.to_csv('wsc.csv')
df3.to_csv('sst.csv')
df4.to_csv('agn.csv')

