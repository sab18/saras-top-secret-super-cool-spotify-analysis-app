import pandas as pd
import json
import os

def get_df(file_name,folder_name):
    file_path = os.path.join(folder_name, file_name)
    abs_file_path = os.path.abspath(file_path)
    file=open(abs_file_path,'r',encoding='utf-8')
    data=json.load(file)
    df=pd.json_normalize(data)
    return df


