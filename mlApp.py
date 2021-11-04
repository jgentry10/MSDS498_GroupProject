#Import dependencies
import pandas as pd
#from tqdm import tqdm_notebook as tqdm
import numpy as np
import os
import tabulate
import json
import pickle
from gensim.models import Word2Vec

infile = open('geekyfile','rb')
data_dict = pickle.load(infile)
infile.close()

model_filename = "item2vec.200d.model"
model = Word2Vec.load(model_filename)

def to_product_name(id, columns='product_name'):
    return data_dict['products'][data_dict['products'].product_id==id][columns].values.tolist()[0]
    
def most_similar_readable(model, product_id, topn=10):
    similar_list = [(product_id, 1.0)] + model.wv.most_similar(str(product_id), topn=topn)
    return pd.DataFrame([( to_product_name(int(id)), int(id), similarity ) for (id, similarity) in similar_list],
                        columns=['product', 'product_id', 'similarity'])

def print_df(df, rows = 10, print_df_mode='psql'):
    if print_df_mode == 'psql':
        print(tabulate(df.head(rows), headers='keys', tablefmt='psql'))
    else:
        display(df.head(rows))
    print(f'{len(df)} rows x {len(df.columns)} columns')
    
# Find similar products
product_id = 24116
df1 = most_similar_readable(model, product_id)

# convert the dataframe to a dictionary and then dump dictionary to json
d = df1.to_dict(orient='records')
j = json.dumps(d)

print(j)
