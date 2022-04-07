import os
import pandas as pd

folder = os.path.join(os.getcwd(),'..','join')

with open(os.path.join(folder,'News.csv'), 'a', encoding='utf-8') as f1:
    with open(os.path.join(folder,'News2.csv'), 'r', encoding='utf-8') as f2:

        f1.write('\n')
        f1.write(f2.read())
    

    

