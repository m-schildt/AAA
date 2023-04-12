import pandas as pd
import numpy as np



def search_nace(code):
    code_list = pd.read_csv('WZ_2008-DE-2023-04-11-Gliederung.csv',encoding='utf-8-sig', delimiter=';')
    code_list = code_list.iloc[8:]
    code_list['Unnamed: 3'] = np.where(code_list['Unnamed: 1'] == '1', code_list['Unnamed: 2'],np.NaN)
    code_list['Unnamed: 3'] = code_list['Unnamed: 3'].fillna(method='ffill')


    try:
        search = code_list[code_list["Unnamed: 2"] == code].iloc[:1,0]
        search = search.values[0]
        search = search.split(".")[0]

        result_lv2 = code_list[code_list['Klassifikation der Wirtschaftszweige, Ausgabe 2008'] == search].iloc[:1,2].values[0]

        result_lv1 = code_list[code_list["Unnamed: 2"] == code].iloc[:1,3].values[0]

        return result_lv1, result_lv2
    except:
        return code