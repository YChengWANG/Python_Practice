# Preprocessing data 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

csv_path = 'MachineLearning\day3-Multiple Linear Regression\Social_Network_Ads.csv'
dataset = pd.read_csv(csv_path)
X = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values

from sklearn import model_selection
X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=0.2)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Logistic regression model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,y_train)
#print(classifier.coef_,classifier.intercept_)

# Prediction
y_pred = classifier.predict(X_test)

# Evaluating the Prediction
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
#print(cm)

# Visualization
plt.subplot(211)
plt.scatter(X_train[:,0],X_train[:,1],c=y_train)
x1_plot = np.linspace(min(X_train[:,0]),max(X_train[:,0]),100)
x2_plot = (-classifier.coef_[0][0]*x1_plot-classifier.intercept_[0])/classifier.coef_[0][1]
plt.plot(x1_plot,x2_plot)
plt.title("Logistic Regression(Training set)")
plt.subplot(212)
plt.scatter(X_test[:,0],X_test[:,1],c=y_test)
plt.plot(x1_plot,x2_plot)
plt.title("Logistic Regression(Test set)")
plt.show()
