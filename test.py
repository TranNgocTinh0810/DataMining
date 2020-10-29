# Load a CSV file
import csv
from csv import reader
def load_csv (filename):
    file=open(filename,"r")
    lines =reader(file)
    dataset=list(lines)
    return dataset
def is_number(s):
    if(s!=''):
        try:
            float(s)
            return True
        except ValueError:
            return False
# Load dataset
'''filename = 'house-prices.csv'
dataset = load_csv(filename)
#print ('Loaded data file{0} with {1} rows and {2} columns'.format(filename,len(dataset), len(dataset[0])))
print(dataset[0][0])'''
data=[[123],[234],[345]]
with open('Cau 3.1.csv', 'w') as f:
    write = csv.writer(f)
    print("dt2", data)
    write.writerows(data)
    f.close()
a=load_csv('Cau 3.1.csv')
print(a.__len__(),data.__len__())

import pandas as pd

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('GFG.csv')
