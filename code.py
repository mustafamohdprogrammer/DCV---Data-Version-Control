import pandas as pd
import os

data = {
    'Name':['Alice','Bob','John'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}

df = pd.DataFrame(data)

new_row_loc = {'Name' : 'David', 'Age' : 28, 'City' : 'Houston'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'Name' : 'Dave', 'Age' : 29, 'City' : 'Houston'}
df.loc[len(df.index)] = new_row_loc2


data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

file_path = os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)
print(f'csv file saved at {file_path}')