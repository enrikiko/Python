from flask import Flask, render_template, request
import numpy as ny
#import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0, 1))
dataset_trainning = pd.read_csv("Google_Stock_Price_Train.csv")
trainning_set = dataset_trainning.iloc[:, 1:2].values
print(trainning_set)
trainning_set_scaled = sc.fit_transform(trainning_set)
print(trainning_set_scaled)

# app = Flask(__name__)
#
# @app.route('/example/')
# def example():
#     return {'hello': 'world'}
#
# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')
