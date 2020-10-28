import sys
import csv
from csv import reader
import pandas as pd
import numpy as np
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset
def list_missing(dataset):
    list_missing_col=[]
    for col in range(0,len(dataset[0]),1):
        for row in range(0,len(dataset),1):
            if ( dataset[row][col]==''):
                list_missing_col.append(col)
                break
    print("Cac Cot Bi Thieu Du Lieu La : ",list_missing_col)
    return list_missing_col
def count_missing_col(dataset):
    count=0
    for row in range(0,len(dataset),1):
        for col in range(0,len(dataset[0]),1):
            if ( dataset[row][col]==''):
                count+=1
                break
    print("Tong So Cot Thieu Du Lieu La ",count)
    return count
def is_number(s):
    '''
    check Int,float or String
    :param s: list
    :return: True,False
    '''
    for i in s:
        if(s!=''):
            try:
                float(i)
                return True
            except ValueError:
                return False

def col_mean(dataset):
    sum=0
    length=0
    for i in dataset:
        if( i!= ''):
            sum=sum+int(i)
            length+=1
    return sum / length
def col_mode(dataset):
    max=0
    result=''
    for i in dataset:
        if dataset.count(i) > max:
            max=dataset.count(i)
            result=i
    return result
def fill_missing(dataset):
    print("dt1",dataset.__len__())
    SubDataset=[]  #Check Str or Int,Float
    count1=0
    for col in list_missing(dataset):
        temp1=[]
        for row in range(0, len(dataset), 1):
            if(dataset[row][col]!=''):
                #SubDataset[count1].append(dataset[row][col])
                temp1.append(dataset[row][col])
        SubDataset.append(temp1)
    temp=[]
    for i in range(0,SubDataset.__len__(),1):
        if is_number(SubDataset[i]):
            SubDataset[i]=col_mean(SubDataset[i])
        else:
            SubDataset[i]=col_mode(SubDataset[i])
    i = 0
    for col in list_missing(dataset):
        for row in range(0, len(dataset), 1):
            if(dataset[row][col]==''):
                dataset[row][col]=SubDataset[i]
        i=i+1
    print("dt3",dataset.__len__())
    return dataset
def run(i,dataset):
    if(i=='list-missing'):
        list_missing(dataset)
    if(i=='count_missing_col'):
        count_missing_col(dataset)
    if(i=='fill_missing'):
        dataset2=fill_missing(dataset)
        with open('Cau 3.3.csv', 'w') as f:
            write = csv.writer(f,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            print("dt2",dataset2.__len__())
            write.writerows(dataset2)


dataset=load_csv(sys.argv[2])
run(sys.argv[1],dataset)


