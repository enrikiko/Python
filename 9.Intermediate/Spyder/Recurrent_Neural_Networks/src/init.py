from flask import Flask, render_template, request
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

sc = MinMaxScaler(feature_range=(0, 1))
data_set_training = pd.read_csv("Google_Stock_Price_Train.csv")
training_set = data_set_training.iloc[:, 1:2].values
# print(training_set)
training_set_scaled = sc.fit_transform(training_set)
# print(training_set_scaled)
x_train = []
y_train = []
for i in range(60, 1258):
    x_train.append(training_set_scaled[i - 60:i, 0])
    y_train.append(training_set_scaled[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Reshaping
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Initialising the RNN
regressor = Sequential()
# First layer
regressor.add(LSTM(unit=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
regressor.add(Dropout(rate=0.2))
# Second layer
regressor.add(LSTM(unit=50, return_sequences=True))
regressor.add(Dropout(rate=0.2))
# Third layer
regressor.add(LSTM(unit=50, return_sequences=True))
regressor.add(Dropout(rate=0.2))
# Last layer
regressor.add(LSTM(unit=50))
regressor.add(Dropout(rate=0.2))

regressor.add(Dense(units=1))

regressor.compile(optimizer="adam", loss="mean_squared_error")

regressor.fit(x_train, y_train, epochs=100, batch_size=32)
# app = Flask(__name__)
#
# @app.route('/example/')
# def example():
#     return {'hello': 'world'}
#
# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')
