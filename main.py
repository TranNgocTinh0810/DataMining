import sys
import csv
from csv import reader
import pandas as pd

def load_csv(filename):
    '''
    Load file csv
    :param filename: string
    :return:
    '''
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
            if ( dataset[row][col]==''):             #Duyệt ma trận theo cột,nếu giá trị cột nào thiếu sẽ thêm
                                                     #hàng đó vào 1 list.Sau đó chuyển đến hàng tiếp theo
                list_missing_col.append(col)
                break
    print("Cac Cot Bi Thieu Du Lieu La : ",list_missing_col)
    return list_missing_col
def count_missing_row(dataset):
    '''
    Đếm số dòng bị thiếu dữ liệu.
    :param dataset: list
    :return: int
    '''
    count=0
    for row in range(0,len(dataset),1):
        for col in range(0,len(dataset[0]),1):     #Duyệt ma trận theo hàng
            if ( dataset[row][col]==''):           #Nếu giá trị thiếu sẽ tăng biến count lên 1
                count+=1
                break                              #Chuyển đến hàng tiếp theo
    print("Tong So Cot Thieu Du Lieu La ",count)
    return count
def is_number(s):              #Hàm kiểm tra là giá trị numeric hay categorical
    '''
    check Int,float or String
    :param s: list
    :return: True,False
    '''
    for i in s:
        if(s!=''):                         #Kiểm tra giá trị rỗng
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
            sum=sum+int(i)                            #Tính tổng các giá trị numeric
            length+=1
    return sum / length                               #Chia cho độ dài -> giá trị mean
def col_mode(dataset):
    '''
    Mode Col: if values of col are categorical
    :param dataset: list
    :return: string
    '''
    max=0                                             #Khởi tạo giá trị max =0
    result=''
    for i in dataset:
        if dataset.count(i) > max:                    #Nếu số lần lặp lại > max
            max=dataset.count(i)                      # -> giá trị max mới
            result=i
    return result                                      # Trả vê giá trị Mode
def fill_missing(dataset):
    '''
    Điền giá trị bị thiếu bằng phương pháp mean, median (cho thuộc tính numeric) và mode
    (cho thuộc tính categorical). Lưu ý: khi tính mean, median hay mode các bạn bỏ qua giá
    trị bị thiếu.
    :param dataset:
    :return:
    '''
    SubDataset=[]  #Check Str or Int,Float
    count1=0
    for col in list_missing(dataset):                   #Vòng for đầu tìm ra các cột có giá trị thiếu
        temp1=[]                                        #Và thêm các giá trị cột đó vào SubDataSet
        for row in range(0, len(dataset), 1):
            if(dataset[row][col]!=''):
                #SubDataset[count1].append(dataset[row][col])
                temp1.append(dataset[row][col])
        SubDataset.append(temp1)
    temp=[]
    for i in range(0,SubDataset.__len__(),1):
        if is_number(SubDataset[i]):
            SubDataset[i]=col_mean(SubDataset[i])                  #Nếu cột là numeric -> cột đó sẽ là mean
        else:
            SubDataset[i]=col_mode(SubDataset[i])                  #Ngược lại : Mode
    i = 0
    for col in list_missing(dataset):
        for row in range(0, len(dataset), 1):
            if(dataset[row][col]==''):
                dataset[row][col]=SubDataset[i]                     #Điền các giá trị từ SubDataset vào vị trí thiếu của dữ liệu ban đầu
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
    list_missing_row = {}                                     #Khởi tạo 1 dict để lưu giá key là row : values là số giá trị thiếu
    for row in range(0, len(dataset), 1):                     #Vòng lặp for đầu tìm ra giá trị thiếu của mỗi hàng
        for col in range(0, len(dataset[0]), 1):
            if (dataset[row][col] == ''):
                if(row not in list_missing_row):
                    list_missing_row[row]=1
                else:
                    list_missing_row[row]+=1
    print(list_missing_row)
    lengthrow=dataset[0].__len__()
    for row in list(list_missing_row.keys()):
        if((list_missing_row[row]/lengthrow)<=(scale/100)):           #Kiểm tra hàng nào có giá trị thiếu bé hơn scale
            del list_missing_row[row]                                 #Delele hàng đó

    check=0
    for row in list(list_missing_row.keys()):                         # Xóa các hàng đủ điều kiện > scale
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
    return [row[:i] + row[i + 1:] for row in mat]       #Hàm xóa một cột trong ma trận ở cột thứ i
def del_col_scale(dataset,scale):
    '''
    Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các cột bị
    thiếu hơn 50% giá trị các thuộc tính)
    :param dataset: list
    :param scale: int.example 50-> meaning 50 percent
    :return: List
    '''
    scale=int(scale)
    list_missing_col = {}                                           #Khởi tạo 1 list.Giá trị key: tên hàng .Giá trị values : số giá trị thiếu
    for col in range(0, len(dataset[0]), 1):                        #Vòng lặp for đầu tìm giá trị thiếu của mỗi cột
        for row in range(0, len(dataset), 1):
            if (dataset[row][col] == ''):
                if(col not in list_missing_col):
                    list_missing_col[col]=1
                else:
                    list_missing_col[col]+=1
    print(list_missing_col)
    lengthcol=dataset.__len__()
    for col in list(list_missing_col.keys()):                        #Vòng lặp for 2 kiểm tra cột nào có giá trị thiếu lớn hơn scale
        if((list_missing_col[col]/lengthcol)<=(scale/100)):
            del list_missing_col[col]
    check=0
    for col in list(list_missing_col.keys()):                        #Xóa dòng đó đi
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
    set_temp=set()                                    #Dùng tính chất của kiểu dữ liệu set để loại bỏ trùng
    for row in dataset:                              #Duyệt ma trận theo dòng
        temp=tuple(row)
        if temp not in set_temp:                      #Nếu chưa có thì thêm hàng vào
            set_temp.add(temp)
        else :
            dataset.remove(row)                       #Nếu đã có thì xóa dòng đó đi
    return dataset
pos_inf = 1000000000000
nega_inf=-1000000000000
def minmax_normalize(dataset,properties,NewMin,NewMax):
    '''
    Câu 7-A
    Chuẩn hóa một thuộc tính numeric bằng phương pháp min-max
    :param dataset: List of List
    :param properties: string
    :param NewMin: float
    :param NewMax: float
    :return: list of list
    '''
    min=pos_inf
    col = dataset[0].index(properties)
    for i in range(1, len(dataset),1):                      #Vòng for đầu tìm min của từng cột
        if (is_number(dataset[i][col])):
            if float(dataset[i][col])<min:
                min=float(dataset[i][col])
    max = nega_inf
    for i in range(1, len(dataset), 1):                    #Vòng for thứ 2 tìm max của từng cột
        if (is_number(dataset[i][col])):
            if float(dataset[i][col]) > max:
                max = float(dataset[i][col])

    for row in range(1,len(dataset),1):                   #Áp dụng công thức chuẩn hóa min_max
        if is_number(dataset[row][col]):
            dataset[row][col]=((float(dataset[row][col])-min)/(max-min))*((float(NewMax)-float(NewMin))+float(NewMin))
    return dataset
def standard_deviation(dataset):
    '''

    Hàm tính độ lệch chuẩn
    :param dataset: List
    :return: int
    '''
    mean=col_mean(dataset)
    sum=0
    n=0
    for i in dataset:
        if i!='':
            sum=sum+pow(int(i)-mean,2)                    #Áp dụng công thức tìm độ lệch chuẩn
            n=n+1
    return pow(sum/(n-1),1/2)
def z_score(dataset,properties):
    '''
    Câu 7-B
    Chuẩn hóa một thuộc tính numeric bằng phương pháp Z-score
    :param dataset: list
    :param properties: string
    :return:
    '''
    col_index = dataset[0].index(properties)
    col=[]
    for row in range(1,len(dataset),1):
        col.append(dataset[row][col_index])
    mean=col_mean(col)                               #tìm mean của cột đang xét
    sd=standard_deviation(col)                       #Tìm độ lệch chuẩn của cột đang xét
    for row in range(1, len(dataset), 1):
        if dataset[row][col_index]!='':
            dataset[row][col_index]=(float(dataset[row][col_index])-mean)/sd       #Áp dụng công thức chuẩn hóa z-Score
    return dataset
def run_2_parameter(i,dataset):
    '''
    Hàm chạy tham số dòng lệnh với tham số là 2
    :param i: string
    :param dataset: list of list
    :return:file csv
    '''
    if(i=='list_missing'):
        list_missing(dataset)
    elif(i=='count_missing_row'):
        count_missing_row(dataset)
    elif(i=='fill_missing'):
        dataset2=fill_missing(dataset)
        df = pd.DataFrame(dataset2)
        df.to_csv("Cau3_3.csv",index=False,header=False)
    elif(i=='remove_duplicates'):
        dataset2=remove_duplicates(dataset)
        df = pd.DataFrame(dataset2)
        df.to_csv("Cau3_6.csv",index=False,header=False)

def run_3_parameter(x,y,dataset):
    '''
    Hàm chạy tham số dòng lệnh với tham số là 3
    :param x: string
    :param y: string
    :param dataset: list of list
    :return: file csv
    '''
    if(x=='del_row_scale'):
        dataset=del_row_scale(dataset,y)
        df=pd.DataFrame(dataset)
        df.to_csv("Cau3_4.csv",index=False,header=False)
    elif (x == 'del_col_scale'):
        dataset = del_col_scale(dataset, y)
        df = pd.DataFrame(dataset)
        df.to_csv("Cau3_5.csv",index=False,header=False)
    elif (x == 'z_score'):
        dataset = z_score(dataset,y)
        df = pd.DataFrame(dataset)
        df.to_csv("Cau3_7_b.csv", index=False, header=False)

def run_5_parameter(x,y,z,t,dataset):
    '''
    Hàm chạy tham số dòng lệnh với tham số là 5
    :param x: string
    :param y: string
    :param z: string
    :param t: string
    :param dataset: list of list
    :return:file csv
    '''
    if (x=='minmax_normalize'):
        dataset=minmax_normalize(dataset,y,z,t)
        df = pd.DataFrame(dataset)
        df.to_csv("Cau3_7_a.csv", index=False, header=False)

try:
    if(sys.argv.__len__()==3):
        dataset = load_csv(sys.argv[2])
        run_2_parameter(sys.argv[1],dataset)
    elif (sys.argv.__len__()==4):
        dataset = load_csv(sys.argv[3])
        run_3_parameter(sys.argv[1],sys.argv[2],dataset)
    elif (sys.argv.__len__()==6):
        dataset=load_csv(sys.argv[5])
        run_5_parameter(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],dataset)
except:
    print("Tham So Khong Phu Hop")

'''
Ví dụ tập csv là test.csv

Chức năng 1 : python3 main.py list_missing test.csv

Chức năng 2 : python3 main.py count_missing_row test.csv

Chức năng 3 : python3 main.py fill_missing test.csv

Chức năng 4 : python3 main.py del_row_scale 15 test.csv   

                      Với 15 là 15%.Sẽ xóa các dòng thiếu nhiều hơn 15 % dữ liệu 

Chức năng 5 : python3 main.py del_col_scale 15 test.csv   

                       Với 15 là 15%.Sẽ xóa các dòng thiếu nhiều hơn 15 % dữ liệu

Chức năng 6 : python3 main.py remove_duplicates test.csv


Chức năng 7 :
•	  Z-Score:               python3 main.py z_score diem1 test.csv

                 
•	Min-Max:               python3 main.py minmax_normalize  diem1 0 1 test.csv      

Với diem1 là thuộc tính ta muốn chuẩn hóa 
0 là giá trị Min

1 là giá trị Max

'''



