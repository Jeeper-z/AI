
from flask import Flask

app = Flask(__name__)   
@app.route('/')
def home():
    return "Hello, World!"




@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

app.run(debug=True)