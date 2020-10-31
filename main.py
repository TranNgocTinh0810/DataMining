import sys
import csv
import operator
from csv import reader
import pandas as pd
import numpy as np
def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset
def list_missing(dataset):
    '''
    Liệt kê các cột bị thiếu dữ liệu.
    :param dataset: List
    :return: List
    '''
    list_missing_col=[]
    for col in range(0,len(dataset[0]),1):
        for row in range(0,len(dataset),1):
            if ( dataset[row][col]==''):
                list_missing_col.append(col)
                break
    print("Cac Cot Bi Thieu Du Lieu La : ",list_missing_col)
    return list_missing_col
def count_missing_col(dataset):
    '''
    Đếm số dòng bị thiếu dữ liệu.
    :param dataset: list
    :return: int
    '''
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
    '''
    Mode Col: if values of col are numeric
    :param dataset: List
    :return: float
    '''
    sum=0
    length=0
    for i in dataset:
        if( i!= ''):
            sum=sum+int(i)
            length+=1
    return sum / length
def col_mode(dataset):
    '''
    Mode Col: if values of col are categorical
    :param dataset: list
    :return: string
    '''
    max=0
    result=''
    for i in dataset:
        if dataset.count(i) > max:
            max=dataset.count(i)
            result=i
    return result
def fill_missing(dataset):
    '''
    Điền giá trị bị thiếu bằng phương pháp mean, median (cho thuộc tính numeric) và mode
    (cho thuộc tính categorical). Lưu ý: khi tính mean, median hay mode các bạn bỏ qua giá
    trị bị thiếu.
    :param dataset:
    :return:
    '''
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

def del_row_scale(dataset,scale):
    '''
    Xóa các dòng bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các dòng bị
    thiếu hơn 50% giá trị các thuộc tính)
    :param dataset: list
    :param scale: int.example 50-> meaning 50 percent
    :return: List
    '''
    scale=int(scale)
    list_missing_row = {}
    for row in range(0, len(dataset), 1):
        for col in range(0, len(dataset[0]), 1):
            if (dataset[row][col] == ''):
                if(row not in list_missing_row):
                    list_missing_row[row]=1
                else:
                    list_missing_row[row]+=1
    print(list_missing_row)
    #value=list(list_missing_row.values())
    #print(max(value))
    lengthrow=dataset[0].__len__()
    for row in list(list_missing_row.keys()):
        if((list_missing_row[row]/lengthrow)<=(scale/100)):
            del list_missing_row[row]

    check=0
    for row in list(list_missing_row.keys()):
        dataset.pop(row-check)
        check=check+1

    print(list_missing_row)
    print(list_missing_row.__len__())
    print(dataset.__len__())
    print(dataset)
    return dataset

def delcolumn(mat, i):
    '''
    Xóa cột thứ i của ma trận mat
    :param mat: List of list
    :param i: int
    :return: List of List
    '''
    return [row[:i] + row[i + 1:] for row in mat]
def del_col_scale(dataset,scale):
    '''
    Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các cột bị
    thiếu hơn 50% giá trị các thuộc tính)
    :param dataset: list
    :param scale: int.example 50-> meaning 50 percent
    :return: List
    '''
    scale=int(scale)
    list_missing_col = {}
    for col in range(0, len(dataset[0]), 1):
        for row in range(0, len(dataset), 1):
            if (dataset[row][col] == ''):
                if(col not in list_missing_col):
                    list_missing_col[col]=1
                else:
                    list_missing_col[col]+=1
    print(list_missing_col)
    #value=list(list_missing_row.values())
    #print(max(value))
    lengthcol=dataset.__len__()
    for col in list(list_missing_col.keys()):
        if((list_missing_col[col]/lengthcol)<=(scale/100)):
            del list_missing_col[col]
    check=0
    for col in list(list_missing_col.keys()):
        dataset=delcolumn(dataset,col-check)
        check=check+1

    print(list_missing_col)
    print(list_missing_col.__len__())
    print(dataset[0].__len__())
    print(dataset)
    return dataset
def remove_duplicates(dataset):
    '''
    Xóa các mẫu bị trùng lặp.
    :param dataset: List of list
    :return: list of list
    '''
    set_temp=set()
    for row in dataset:
        temp=tuple(row)
        if temp not in set_temp:
            set_temp.add(temp)
        else :
            dataset.remove(row)
    return dataset

def run_2_parameter(i,dataset):
    if(i=='list-missing'):
        list_missing(dataset)
    elif(i=='count_missing_col'):
        count_missing_col(dataset)
    elif(i=='fill_missing'):
        dataset2=fill_missing(dataset)
        df = pd.DataFrame(dataset2)
        df.to_csv("Cau3_3.csv",index=False,header=False)
    elif(i=='remove_duplicates'):
        dataset2=remove_duplicates(dataset)
        df = pd.DataFrame(dataset2)
        df.to_csv("Cau3_6.csv",index=False,header=False)
def run_3_parameter(x,y,dataset):
    if(x=='del_row_scale'):
        dataset=del_row_scale(dataset,y)
        df=pd.DataFrame(dataset)
        df.to_csv("Cau3_4.csv",index=False,header=False)
    if (x == 'del_col_scale'):
        dataset = del_col_scale(dataset, y)
        df = pd.DataFrame(dataset)
        df.to_csv("Cau3_5.csv",index=False,header=False)



if(sys.argv.__len__()==3):
    dataset = load_csv(sys.argv[2])
    run_2_parameter(sys.argv[1],dataset)
elif (sys.argv.__len__()==4):
    dataset = load_csv(sys.argv[3])
    run_3_parameter(sys.argv[1],sys.argv[2],dataset)


