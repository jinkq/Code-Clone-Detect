import numpy as np

def getSimilarity(dict):
    similarityDict={}
    for filename, featureVec in dict.items():
        for filename2, featureVec2 in dict.items():
            if filename!=filename2 and ((filename,filename2) not in similarityDict) and ((filename2,filename) not in similarityDict):
                if isClone(filename,filename2):
                    clone=1
                else:
                    clone=0
                similarityDict[filename,filename2]=[getDot(featureVec,featureVec2)/(getMod(featureVec)*getMod(featureVec2)),clone]

    return(similarityDict)

def getDot(vec1, vec2):
    sum=0
    for i in range(0,len(vec1)):
        sum += (vec1[i]*vec2[i])
    return sum

def getMod(vec):
    sum=0
    for item in vec:
        sum+=(item*item)
    return sum**0.5

def isClone(filename1,filename2):
    dir1=filename1.split('\\')[1]
    dir2=filename2.split('\\')[1]
    if dir1==dir2:
        return True
    else:
        return False

def getCloneSimilarity(similarityDict):
    cloneSimilarityList=[]
    for row in similarityDict.values():
        if row[1]==1:
            cloneSimilarityList.append(row[0])
    return cloneSimilarityList

def getNotCloneSimilarity(similarityDict):
    notCloneSimilarityList=[]
    for row in similarityDict.values():
        if row[1]==0:
            notCloneSimilarityList.append(row[0])
    return notCloneSimilarityList