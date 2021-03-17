# Process the Data
import numpy as np 
import pandas as pd 
import sklearn as sk
csv_path = 'MachineLearning\day2-Simple-Linear-Regression\studentscores.csv'
dataset = pd.read_csv(csv_path)
Hours = dataset.iloc[:,:1].values
Scores = dataset.iloc[:,1].values
# X = dataset.iloc[:,:].values
# y = np.zeros(X.shape[0])
#print(Hours.reshape(1,-1),Scores)
from sklearn import model_selection
Hours_train,Hours_test,Scores_train,Scores_test = model_selection.train_test_split(Hours,Scores,test_size=0.2)
#print(Hours_train,Hours_test,Scores_train,Scores_test,sep='\n')

# Fitting Simple Linear Regression Model to the Training Set
from sklearn import linear_model
Lreg = linear_model.LinearRegression()
Lreg = Lreg.fit(Hours_train,Scores_train)
#print(Lreg)

# Predict the result
Scores_predict = Lreg.predict(Hours_test)

# Visualization
import matplotlib.pyplot as plt
plt.scatter(Hours_train,Scores_train,color='red')
plt.scatter(Hours_test,Scores_test,color='green')
plt.plot(Hours_test,Scores_predict,color='blue')
plt.title('Linear Regression')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()