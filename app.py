import flask
import os

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    """Login Form"""
flask.render_template('login.html')
    
name = request.form['username']
pipeline = pickle.load(open('pickle/user_based_recomm.pkl', 'rb'))
sr = pipeline.loc[name].sort_values(ascending=False)[0:20] ## series
top_20_products = pd.DataFrame({'name':sr.index})
return  render_template('view.html',tables=[top_20_products.to_html(classes='name')], titles = ['NAN', 'Top 20 Prediction'])


if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    


