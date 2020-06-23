import os
import re
import csv
import pandas as pd
import math


def readFile(path):
    Filelist = []    
    for home, dirs, files in os.walk(path):         
        for filename in files:             
            # 文件名列表，包含完整路径             
            Filelist.append(os.path.join(home, filename))
    
    vectorList=[]
    for file in Filelist:
        # print(file)
        # print(txt2vec(file))
        vectorList.append(txt2vec(file))
        # store2csv(file,txt2vec(file))
    
    tfidf_process(vectorList)

    i=0
    for file in Filelist:
        store2csv(file[3:],vectorList[i],path)
        i+=1

    # for vec in vectorList:
    #     print(vec)
    # print('----------------------------')
    
def store2csv(filename,featureVec,path):
    with open(path+'.csv','a',encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([filename,featureVec])

def getDict(path):
    df=pd.read_csv(path+".csv",header=None)
    df.columns=['filename', 'featureVec']
    # print(df)

    dict={}
    
    for index, row in df.iterrows():
        featureVec=row['featureVec'].split(',')
        featureVec[-1] = featureVec[-1][:-1]
        featureVec[0] = featureVec[0][1:]
        
        featureVec = [ float(x) for x in featureVec ]
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

def tfidf_process(vectorList:list):
    # 外层遍历每一个词
    for i in range(0, len(vectorList[0])):
        count = 0
        #内层遍历所有向量，看看这个词出现了多少次
        for vec in vectorList:
            if vec[i] != 0:
                count = count + 1
        #然后每一个分量都要乘上相应的idf值
        if count!=0:
            idf = math.log(len(vectorList)/count)
            for vec in vectorList:
                vec[i] = vec[i] * idf



if __name__ == "__main__":
    path = "test"
    readFile(path)
    dict=getDict()