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
'''data=[[123],[234],[345]]
with open('Cau 3.1.csv', 'w') as f:
    write = csv.writer(f)
    print("dt2", data)
    write.writerows(data)
    f.close()'''


import pandas as pd
df=pd.read_csv('test.csv',skiprows=0)
#df.rename(columns={'Id':'I_d'},inplace=True)
df[(df.SalePrice > '1') & (df.SaleCondition < 'B')]

print(df)



