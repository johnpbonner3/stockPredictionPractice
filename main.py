# NeuralNine practice

# Copied from Youtube
#John Bonner
# 3/31/21

import pandas as pd
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
#Supposed to have tensorflow - but I have an AMD GPU and it does not support CUDA.
#Will see if I can workaround


    #Load data
company = 'FB'

start = dt.datetime(2012,1,1)
end = dt.datetime(2021,1,1)

data = web.DataReader(company, 'yahoo', start, end)

#Prepare Data

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

prediction_days = 60

xtrain = []
ytrain = []

for x in range(prediction_days, len(scaled_data)):
    xtrain.append(scaled_data[x-prediction_days:x, 0])
    ytrain.append(scaled_data[x,0])

xtrain, ytrain = np.array(xtrain), np.array(ytrain)

xtrain = np.reshape(xtrain, (xtrain.shape[0], xtrain.shape[1], 1))

#here is where I run into trouble.




