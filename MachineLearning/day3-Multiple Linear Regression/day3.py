# Preprocess the data
import numpy as np 
import pandas as pd 

csv_path = 'MachineLearning\day3-Multiple Linear Regression\Social_Network_Ads.csv'
dataset = pd.read_csv(csv_path)
X = dataset.iloc[:,:4].values
y = dataset.iloc[:,-1].values
#print(X,y,sep='\n\n')
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le = LabelEncoder()
X = X[:,1:]
X[:,0] = le.fit_transform(X[:,0])
# print(X)
# oe = OneHotEncoder()
# X = oe.fit_transform(X).toarray()
encoder = ColumnTransformer(
    [('onehotencoder',OneHotEncoder(),[0])],remainder="passthrough"
)
X = encoder.fit_transform(X)
#print(X)

# Fiting out model to the training set
from sklearn import model_selection
X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.2)
from sklearn import linear_model
regressor = linear_model.LinearRegression()
regressor = regressor.fit(X_train,y_train)

# Predict the test Result
y_predict = regressor.predict(X_test)

# Visualization
import matplotlib.pyplot as plt
