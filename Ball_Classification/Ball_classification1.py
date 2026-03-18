# Steps for Machine Learning Application

# Step 1 : Data Gathering or Data Collection
# Step 2 : Data Anaysis
# Step 3 : Data Cleaning
# Step 4 : Model Selection
# Step 5 : Model Training
# Step 6 : Model Testing / Evaluation
# Step 7 : Model Improvement
# Step 8 : Prediction or deployment
    

import sklearn

def main():
    print("Ball classification case study")

    #Data gathering 

    Features = [[35 , "Rough"] , [47,"Rough"] , [90,"Smooth"] , [48 , "Rough"] ,[90,"Smooth"] , [35,"Rough"] , [92 , "Smooth"] , [35,"Rough"], [35,"Rough"], [35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"] , [95 ,"Smooth"]]
    Labels = ["tennis","tennis","cricket","tennis","cricket","tennis","cricket","tennis","tennis","tennis","cricket","tennis","cricket","tennis","cricket"]

if __name__ == "__main__":
    main()

#data set size 15