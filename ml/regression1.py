import pandas as pd
import quandl, math, datetime


# to allow us to use arrays
import numpy as np

# preprocessing =- This gives the scaling of data on features. this will help us scale the data
# cross_validation = helps us training and testing. It will help us split the data for training and testing
# cross_validation has been deprecated, instead using model_selection
# svm = support vector machine
from sklearn import preprocessing, model_selection, svm

from  sklearn.linear_model import LinearRegression, LogisticRegression

## Different alogrithms
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

## Quand is a site for getting the stock prices for various companies. It allows for downloading data for 50 times (ie 50 calls per day)
## for anonymous account. For a free account, we need to use the API key
quandl.ApiConfig.api_key = 'zUL_xi9AQLAmyWT8M-7M'
df = quandl.get('WIKI/GOOGL', )

#print(df.head())
## We are interested only in the adjusted price of the stock.
## We derive the high low pct and pct change compared to open and close of the market price.
## These are the features of the data set
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100

df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

## This is for printing the dataset that we get after customizing the headers
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

#print(df.head())

## We will then add a label column which denotes the future price
forecast_col = 'Adj. Close'

## This is to replace the NaN values with -99999 so as to not to lose the data set.
df.fillna(-99999, inplace=True)

## As per this model, we will try to predict the future price of the stock which will be more than 10````% of the current adjusted price
forecast_out = int(math.ceil(0.1*len(df)))

print(forecast_out)

## In effect, it will be the closing price of the stock 10+ days in future
df['label'] = df[forecast_col].shift(-forecast_out)

## if we dont use this dropna, then we will see the NaN values.
df.dropna(inplace=True)
#print(df.head())
#print(df.tail())

## features will be X and labels = y as per good standards

X = np.array(df.drop(['label'], 1))

## This is for getting the forecasted values
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
#X = X[:-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])

#print(len(X), len(y))


## 20% data is being used as testing data.
## It will split the training data and testing data

validation_size = 0.20

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=validation_size)

scoring = 'accuracy'
seed = 1

models = []
models.append(('LNR', LinearRegression(n_jobs=-1)))
#models.append(('LR', LogisticRegression()))
#models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', svm.SVC()))
#models.append(('SVR', svm.SVR()))

#kfold = model_selection.KFold(n_splits=10, random_state=seed)
results = []
names = []
for name, model in models:
#    cv_results = model_selection.cross_val_score(model, X_train.astype('int'), y_train.astype('int'))

    ## We will fit the train data to the classifier
    ## this is for training data
    model.fit(X_train.astype('int'), y_train.astype('int'))

    ## This is for testing data
    accuracy = model.score(X_test.astype('int'), y_test.astype('int')) * 100

    forecast_set = model.predict(X_lately)

    msg = "%s: %f" % (name, accuracy)
    names.append(name)
    print(msg)
#    print(forecast_set, accuracy, forecast_out)

    df['Forecast'] = np.nan
    last_date = df.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        ## Add the values under the different features/ attributes as NaN. The last column is the forecasted value
        df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    print(df.tail())
    df['Adj. Close'].plot()
    df['Forecast'].plot()
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
