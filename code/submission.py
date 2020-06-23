import csv
import pandas as pd

def readFile():
    path='../data/sample_submission.csv'
    df=pd.read_csv(path,encoding='utf-8')

    file1=[]
    file2=[]

    for row in df['id1_id2']:
        file1.append(row.split('_')[0]+'.txt')
        file2.append(row.split('_')[1]+'.txt')
    
    prediction=[0]*len(file1)

    submission=pd.DataFrame({'file1':file1,'file2':file2,'prediction':prediction})
    # submission.columns=['file1', 'file2']
    # submission=[file1,file2,0]
    return(submission)

def modifySubmission(df_test, submission):
    for index, row in df_test.iterrows():
        for index2, row2 in submission.iterrows():
            if (row['file1']==row2['file1'] and row['file2']==row2['file2']) or (row['file1']==row2['file2'] and row['file2']==row2['file1']):
                row2['prediction']=row['prediction']
                break

    return submission