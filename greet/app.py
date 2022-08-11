from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """
    shows welcome
    """
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """
    shows welcome home
    """
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """
    shows welcome back
    """
    return "welcome back"