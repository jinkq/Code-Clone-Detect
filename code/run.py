import preprocess, deal, logistic, submission
import numpy as np


if __name__ == "__main__":
    path = "../train"
    preprocess.readFile(path)
    dict_train=preprocess.getDict(path)
    # print(dict)
    
    # 相似度dict，键是两个文件名，值是[特征向量，是否clone]
    similarityDict_train=deal.getSimilarity(dict_train)
    # print(similarityDict)

    # # 获得所有clone的余弦相似度
    # cloneSimilarityList=deal.getCloneSimilarity(similarityDict)
    # # print(cloneSimilarityList)
    # # 获得所有非clone的余弦相似度
    # notCloneSimilarityList=deal.getNotCloneSimilarity(similarityDict)
    # # print(notCloneSimilarityList)

    # 获得训练集的x和y
    x_train,y_train=deal.getArray(similarityDict_train)

    path = "../test"
    preprocess.readFile(path)
    dict_test=preprocess.getDict(path)
    # print(dict)

    # 测试集
    
    # 相似度dict，键是两个文件名，值是[特征向量]
    similarityDict_test=deal.getSimilarity_test(dict_test)
    # 获得测试集的x和y
    x_test,df_test=deal.getArray_test(similarityDict_test) # df_test是[file1, file2, similarity, prediction]
    y_test=np.zeros(shape=[len(x_test),1]) # 初始化为全0

    # print(similarityDict_test)
    # print(x_train)
    # print(y_train)
    # print(x_test)
    # print(y_test)

    # 预测值
    y_test=logistic.logistic(x_train,y_train,x_test,y_test)
    # print(y_test)
    df_test['prediction']=y_test
    print(df_test)

    df_submission=submission.readFile()
    df_submission=submission.modifySubmission(df_test,df_submission)
    # df_submission.to_csv('sample.csv',encoding='utf-8')
    print(df_submission)