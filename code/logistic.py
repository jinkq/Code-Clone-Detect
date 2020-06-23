from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score

def logistic(x_train,y_train,x_test,y_test):

    lr_model = LogisticRegression() #调用模型，但是并未经过任何调参操作，使用默认值

    lr_model.fit(x_train,y_train) #训练模型

 
    predictions = lr_model.predict(x_test)
    y_test=predictions.reshape(-1,1)
    # print('测试集准确率：', f1_score(y_train, predictions))
    print(lr_model.score(x_test,y_test))
    return y_test
    # print(lr_model.score(x_test,y_test))  #获取测试集的评分
    # print('测试集准确率：', accuracy_score(y_test, predictions))
    