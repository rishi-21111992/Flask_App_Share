import flask
import os

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        pipeline = pickle.load(open('pickle/user_based_recomm.pkl', 'rb'))
        sr = pipeline.loc[name].sort_values(ascending=False)[0:20] ## series
        top_20_products = pd.DataFrame({'name':sr.index})

        reviews = pd.read_csv('dataset/sample30.csv')

        top_20_reviews = reviews[reviews['name'].isin(top_20_products['name'])][['name','reviews_text']]

        transformer = TfidfTransformer()
        loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open('pickle/vector', 'rb')))
        test_data_features = transformer.fit_transform(loaded_vec.fit_transform(top_20_reviews['reviews_text']))
        
        loaded_model = pickle.load(open("pickle/LRModel", 'rb'))
        result1 = loaded_model.predict(test_data_features)
        
        top_20_reviews['sentiment'] = result1.tolist()
        
        top = top_20_reviews.groupby(['name']).mean()
        
        top5 = top.sort_values(by='sentiment',ascending=False)[:5]

        return  render_template('view.html',tables=[top5['name'].to_html(classes='name')], titles = ['NAN', 'Top 5 Prediction'])


if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    