from sklearn import tree
# rough = 1
# smooth = 0

#cricket = 2
#tennis = 1
def main():
    print("Ball classification case study")

    #Data gathering 

    # independent variables
    Features = [[35 , 1] , [47,1] , [90,0] , [48 , 1] ,[90,0] , [35,1] , [92 , 0] , [35,1], [35,1], [35,1],[96,0],[43,1],[110,0],[35,1] , [95 ,0]]

    #dependent variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()
    trainedmodel = modelobj.fit(Features,Labels)
    Result = trainedmodel.predict([[37,1] , [94,0]]) #[1 2]

    print("Model predicts the object as : ",Result);    


if __name__ == "__main__":
    main()

#data set size 15