import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'models/SOT_Trees.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return(flask.render_template('Methodology.html'))

@app.route('/app')
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('product.html'))

    if flask.request.method == 'POST':
         pclass = flask.request.form['pclass']
         survived = flask.request.form['survived']
         sex = flask.request.form['sex']
         age = flask.request.form['age']
         fare = flask.request.form['fare']
         embarked = flask.request.form['embarked']
         Title = flask.request.form['Title']
         relatives = flask.request.form['relatives']

    # Make DataFrame for model
    input_variables = pd.DataFrame([[pclass, survived, sex, age, fare, embarked, Title, relatives]],
                          columns=['pclass', 'survived', 'sex', 'age', 'fare', 'embarked', 'Title', 'relatives'],
                          dtype=float,
                          index=['input'])
    
    # Get the model's prediction
    prediction = model.predict(input_variables)[1]

    '''Render the form again, but add in the prediction and remind user
    of the values they input before
    '''    
    return flask.render_template('product.html', 
                original_input={'pclass':pclass,
                                'sex':sex,
                                'age':age,
                                'fare':fare,
                                'embarked':embarked,
                                'Title':Title,
                                'relatives':relatives},
                result=prediction,)

if __name__ == '__main__':
    app.run(debug=True)