# Apriori
import csv
#import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

# Load the CSV data file using pandas read_csv method
play_tennis = pd.read_csv("IPT\Finals\myDataset.csv")

print(play_tennis.head)


number = LabelEncoder()
play_tennis.Outlook  = number.fit_transform(play_tennis.Outlook)
print(play_tennis.Outlook)
play_tennis.Temp = number.fit_transform(play_tennis.Temp)
print(play_tennis.Temp)
play_tennis.Humidity = number.fit_transform(play_tennis.Humidity)
print(play_tennis.Humidity)
play_tennis.Humidity =  number.fit_transform(play_tennis.Humidity)
play_tennis.Windy = number.fit_transform(play_tennis.Windy)
print(play_tennis.Windy)
play_tennis.Play = number.fit_transform(play_tennis.Play)
print(play_tennis.head)

features = ["Outlook","Temp","Humidity","Windy"]
target = "Play"

print(features)
print(target)

#The X_test and y_test sets are used for testing the model if it's predicting the right outputs/labels.
#we can explicitly test the size of the train and test sets.
features_train, features_test, target_train, target_test = train_test_split(play_tennis[features],play_tennis[target],
                                                                            test_size = 0.20,random_state = 42)

print('\tTraining Features\n ',features_train)
print('\tTesting Features\n ',features_test)
print('\tTraining Target\n ',target_train)
print('\tTesting Target\n ',target_test)


model = GaussianNB()
model.fit(features_train, target_train)

print('\tmodel.fit',   model.fit)
pred = model.predict(features_test)
print(pred)
accuracy = accuracy_score(target_test, pred)
print("\nModel Accuracy = ",accuracy*100,"%")

answer = model.predict([[2,2,1,0]])

if answer == 1:
    print("\nPlay ") 
if answer == 0:
    print("\nNo Play")




                                        





