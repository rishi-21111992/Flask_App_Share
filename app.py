import flask
import os

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
import model

# Create the application.
app = flask.Flask(__name__)

reviews = pd.read_csv('dataset/sample30.csv')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form['username']
        try:
            data = reviews[reviews['reviews_username'] == name]
            
            if not data.empty:
               top_5_product=model.prediction(name)
               
               return  render_template('view.html',tables=[top_5_product.to_html(classes='name')], titles = ['NAN', 'Top 5 Prediction'])
               
            else:
                return 'username not available'

        except:
            return "username not available"


if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    