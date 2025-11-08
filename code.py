import pandas as pd
import os

data = {
    'Name':['Alice','Bob','John'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)


data_dir = 'data'
os.mkdir(data_dir)

file_path = os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)
print(f'csv file saved at {file_path}')