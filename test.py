# Load a CSV file
from csv import reader
def load_csv (filename):
    file=open(filename,"r")
    lines =reader(file)
    dataset=list(lines)
    return dataset
def is_number(s):
    if(s!='')
        try:
            float(s)
            return True
        except ValueError:
            return False
# Load dataset
filename = 'house-prices.csv'
dataset = load_csv(filename)
#print ('Loaded data file{0} with {1} rows and {2} columns'.format(filename,len(dataset), len(dataset[0])))
print(dataset[0][0])



