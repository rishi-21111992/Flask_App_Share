import flask
import os

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
	    

if __name__ == '__main__':
    app.debug=True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    