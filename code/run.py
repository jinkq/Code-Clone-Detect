import preprocess, deal


if __name__ == "__main__":
    path = "../test"
    preprocess.readFile(path)
    dict=preprocess.getDict()
    # print(dict)
    
    # 相似度dict，键是两个文件名，值是[特征向量，是否clone]
    similarityDict=deal.getSimilarity(dict)
    print(similarityDict)

    # 获得所有clone的余弦相似度
    cloneSimilarityList=deal.getCloneSimilarity(similarityDict)
    print(cloneSimilarityList)
    # 获得所有非clone的余弦相似度
    notCloneSimilarityList=deal.getNotCloneSimilarity(similarityDict)
    print(notCloneSimilarityList)