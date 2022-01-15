"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from instagram import getfollowedby, getname


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



#loading the sparse file which have processed features
# Raw File which have missing values , Outlier , ..

# You can python to process and creat final DF or object which then pass in Pickle

# loading the data 
# here i am loading npz , you can load csv , xlsx , databse conenection 
#Xtest_Scenerio1_for_flask  = sparse.load_npz("dataset/Xtest_Scenerio1_for_flask.npz")
# here you can database connector 
# external API (Twitter API )

#Xtest_Scenerio1_for_flask  - holding my data whch will render on UI 

# http:baseurl/age_prediction

@app.route('/login', methods=['POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        pipeline = pickle.load(open('pickle/user_based_recomm.pkl', 'rb'))
        sr = pipeline.loc[name].sort_values(ascending=False)[0:20] ## series
        top_20_products = pd.DataFrame({'name':sr.index})
        return  render_template('view.html',tables=[top_20_products.to_html(classes='name')], titles = ['NAN', 'Top 20 Prediction'])



# Any HTML template in Flask App render_template

if __name__ == '__main__' :
    app.run(debug=True )  # this command will enable the run of your flask app or api
    
    #,host="0.0.0.0")





