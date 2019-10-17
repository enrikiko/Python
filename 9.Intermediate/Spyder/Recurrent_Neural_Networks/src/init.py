from flask import Flask, render_template, request
import numpy as ny
import matplolib.pyplo as plt
import pandas as pd

dataset_trainning = pd.read_csv("Google_Stock_Price_Train.csv")
trainning_set = dataset_trainning.iloc[:, 1:2].values

# app = Flask(__name__)
#
# @app.route('/example/')
# def example():
#     return {'hello': 'world'}
#
# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0')
