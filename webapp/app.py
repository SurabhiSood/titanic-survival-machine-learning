import os
import numpy as np
import flask
import pickle
import pandas as pd
from flask import Flask, render_template, request
import joblib

with open(f'model/trained_knn_model.pkl', 'rb') as f:
    model = joblib.load(f)

app = flask.Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        pclass = flask.request.form['Pclass']
        sex = flask.request.form['Sex']
        age = flask.request.form['Age']
        sibsp = flask.request.form['SibSp']
        parch  = flask.request.form['Parch']
        fare   = flask.request.form['Fare']
        embarked    = flask.request.form['Embarked']
        
        input_variables = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked]],
                                       columns=['Pclass', 'Sex', 'Age', 'SipSp', 'Parch', 'Fare', 'Embarked'],
                                       dtype=float,
                                       index=['input'])

        prediction = model.predict(input_variables)[0]
        if prediction == 1: 
            prediction_stmt = "Great job! You survived the Titanic!"
        else: 
            prediction_stmt = "This will be your last cruise  :( "

        return flask.render_template('index.html',
                                     original_input={'Pclass': pclass,
                                     'Sex': sex,
                                     'Age': age,
                                     'SibSp': sibsp,
                                     'Parch': parch,
                                     'Fare': fare,
                                     'Embarked': embarked},
                                     result=prediction_stmt,
                                     )

@app.route('/about.html')
def about():
    if flask.request.method == 'GET':
        return flask.render_template('about.html')


@app.route('/methodology.html')
def methodology():
    if flask.request.method == 'GET':
        return flask.render_template('methodology.html')

if __name__ == '__main__':
    app.run(debug=True)




