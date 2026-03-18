from sklearn import tree
# rough = 1
# smooth = 0

#cricket = 2
#tennis = 1
def main():
    print("Ball classification case study")

    #Orignal encoded dataset 

    # independent variables
    X = [[35 , 1] , [47,1] , [90,0] , [48 , 1] ,[90,0] , [35,1] , [92 , 0] , [35,1], [35,1], [35,1],[96,0],[43,1],[110,0],[35,1] , [95 ,0]]

    #dependent variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independent variables for training
    Xtrain = [[35 , 1] , [47,1] , [90,0] , [48 , 1] ,[90,0] , [35,1] , [92 , 0] , [35,1], [35,1], [35,1],[96,0],[43,1],[110,0]]

     # Independent variables for testing
    Xtest =[[35,1] , [95 ,0]]

     # dependent variables for training
    Ytrain= [1,1,2,1,2,1,2,1,1,1,2,1,2]

     # dependent variables for testing
    Ytest= [1,2]

    modelobj = tree.DecisionTreeClassifier()
    trainedmodel = modelobj.fit(Xtrain,Ytrain)
    Result = trainedmodel.predict([[35,1]]) #[1 2]

    print(type(Result))

    if Result == 1:
        print("Object looks like tennis ball")
    elif Result == 2:
        print("Object looks like cricket ball")


if __name__ == "__main__":
    main()

#data set size 15