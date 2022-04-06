import os
import pandas as pd

folder = os.path.join(os.getcwd(),'..','data','korpus')
korpus = pd.read_csv(os.path.join(folder,'norm_korpus_clean.csv'))['Word'].to_numpy()

with open(os.path.join(folder,'jo_korpus.txt'), 'w', encoding='utf-8') as f:
    for word in korpus:
        f.write(word)
        f.write('\n')

print('Finished!')