# Import the required libraries 
import numpy as np 
import pandas as pd 

# Import the Data set
csv_path = 'MachineLearning\day1-Data-Preprocessing\Data.csv'
dataset = pd.read_csv(csv_path)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values
#print(X)
#print(Y)

# Handling the missing data
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values = np.nan,strategy = 'mean')
imp_mean.fit(X[:,1:])
X[:,1:] = imp_mean.transform(X[:,1:])
#print(X)

# Encoding categorical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le_x = LabelEncoder()
X[:,0] = le_x.fit_transform(X[:,0])
le_y = LabelEncoder()
Y = le_y.fit_transform(Y)
#print(X)
#print(Y)

# Spliting the dataset into train sets and test sets
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
#print(X_train,X_test,sep='\n\n')

# Feature Scalering
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
#print(sc_x.mean_)
X_test = sc_x.fit_transform(X_test)
#print(sc_x.mean_)
#print(X_train,X_test,sep='\n\n')