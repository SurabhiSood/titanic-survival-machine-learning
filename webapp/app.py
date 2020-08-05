import os
import numpy as np
import flask
import pickle
import pandas as pd
from flask import Flask, render_template, request

# Use pickle to load in the pre-trained model.
with open(f'model/titanic_knn.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

# @app.route('/')
# def index():
#     return(flask.render_template('index.html'))
# if __name__ == '__index__':
#     app.run()

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        pclass = flask.request.form['Pclass']
        sex = flask.request.form['Sex']
        age = flask.request.form['Age']
        sibsp = flask.request.form['SibSp']
        parch  = flask.request.form['Parch']
        fare   = flask.request.form['Fare']
        embarked    = flask.request.form['Embarked']
        
        input_variables = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked]],
                                       columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'],
                                       dtype=float,
                                       index=['input'])

        prediction = model.predict(input_variables)[0]

        return flask.render_template('index.html',
                                     original_input={'Pclass': pclass,
                                     'Sex': sex,
                                     'Age': age,
                                     'SibSp': sibsp,
                                     'Parch': parch,
                                     'Fare': fare,
                                     'Embarked': embarked},
                                     result=prediction,
                                     )

if __name__ == '__index__':
    app.run()




