#Data Mine
#http://youtu.be/p8hle-ni-DM
#http://youtu.be/eRpFC2CKvao?list=PLyBBc46Y6aAz54aOUgKXXyTcEmpMisAq3

import pandas as pd
import pylab
from pandas import *
from pylab import *

#Get Data
data = open(jan6_dataset.csv)

#Read csv
jan6_dataset=read_csv('Documents/jan6_dataset.csv')

#Dataframe
df = pd.Dataframe.from_csv(data, index_col=None)
df
df['Amount_t'].describe()
Amount = sum('AccountNo_t')
grouping -df.groupby['AccountNo_t']
x = 'Volume'
y = 'Amount'
                     
   

#Slicing
jan6_dataset.ix[0:, ['AccountNo_t', 'Amount_t']]

#Search
jan6_dataset['AccountNo_t']=='800242239'

#Use .head and .tail

#Simpleplot
plot(color = 'Red')

#Functional plot
plot(x,y)

#Linear Regression
print __doc__


# Code source: Jaques Grobler
# License: BSD


import pylab as pl
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis]
diabetes_X_temp = diabetes_X[:, :, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X_temp[:-20]
diabetes_X_test = diabetes_X_temp[-20:]

from sklearn.datasets.samples_generator import make_regression

# this is our test set, it's just a straight line with some
# gaussian noise
X, Y = make_regression(n_samples=100, n_features=1, n_informative=1,\
                        random_state=0, noise=35)


# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print 'Coefficients: \n', regr.coef_
# The mean square error
print ("Residual sum of squares: %.2f" %
        np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print ('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
pl.scatter(diabetes_X_test, diabetes_y_test,  color='black')
pl.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
        linewidth=3)

pl.xticks(())
pl.yticks(())

pl.show()

#Scatter plot
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# output = CTR[Amount_t['Total'] < 9999.99]
#output.plot(kind='bar')
