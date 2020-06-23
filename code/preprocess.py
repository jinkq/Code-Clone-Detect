import os
import re
import csv
import pandas as pd


def readFile(path):

    # path = "nju-introdm20/train/train/0ae1" #文件夹目录
    
    # files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # s = []
    # for file in files:  # 遍历文件夹
    #     # print(type(file))
    #     if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
    #         f = open(path+"/"+file)  # 打开文件
    #         iter_f = iter(f)  # 创建迭代器
    #         str = ""
    #         for line in iter_f:  # 遍历文件，一行行遍历，读取文本
    #             str = str + line
    #             s.append(str)  # 每个文件的文本存到list中
    #             print(s)  # 打印结果
    #     else:
    #         print(1111111111111111)
    #         print(path+"/"+file)
    #         readFile(path+"/"+file)
    
    Filelist = []    
    for home, dirs, files in os.walk(path):         
        for filename in files:             
            # 文件名列表，包含完整路径             
            Filelist.append(os.path.join(home, filename))
    
    for file in Filelist:
        print(file)
        print(txt2vec(file))
        store2csv(file,txt2vec(file))
    
def store2csv(filename,featureVec):
    with open('test.csv','a',encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([filename,featureVec])

def getDict():
    df=pd.read_csv("test.csv",header=None)
    df.columns=['filename', 'featureVec']
    print(df)

    dict={}
    
    for index, row in df.iterrows():
        featureVec=row['featureVec'].split(',')
        featureVec[-1] = featureVec[-1][:-1]
        featureVec[0] = featureVec[0][1:]
        
        featureVec = [ int(x) for x in featureVec ]
        dict[row['filename']]=featureVec
    
    return(dict)

# 统计一个文件中keyWords分别的数量为多少
keyWords = ['int', 'long', 'double', 'float', 'char', 'string', 'void',
            'cin', 'scanf', 'cout', 'printf',
            'if', 'else', 'switch', 'case', 'for', 'while', 'continue', 'break', 'return',
            'new', 'delete',
            '\+', '\-', '\*', '\/', '\+\+', '\-\-', '\+=', '=\+', '\-=', '=\-', '=',
            '==', '!=', '<', '>', '<=', '>=',
            '&&', '\|\|', '!']

def txt2vec(path):
    dict = {}
    for key in keyWords:
        dict[key] = 0
    with open(path, 'r', encoding='utf-8') as f:
        fileContent = f.read()
        for key in keyWords:\
            dict[key] = len(re.findall(key, fileContent))
        # 处理有重复的情况
        dict['int'] = dict['int'] - dict['printf']
        dict['\+'] = dict['\+'] - dict['\+\+'] * 2 - dict['\+='] - dict['=\+']
        dict['\-'] = dict['\-'] - dict['\-\-'] * 2 - dict['\-='] - dict['=\-']
        dict['='] = dict['='] - dict['\+='] - dict['=\+'] - dict['\-='] - dict['=\-'] - dict['=='] * 2 - dict['!='] - dict['<='] - dict['>=']
        dict['!'] = dict['!'] - dict['!=']
        return list(dict.values())

if __name__ == "__main__":
    path = "test"
    readFile(path)
    dict=getDict()