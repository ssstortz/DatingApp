"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("login.html")

@app.route('/signup')
def index():
    return render_template("signup.html")

@app.route('/filtr')
def index():
    return render_template("filtr.html")

@app.route('/messages')
def index():
    return render_template("messages.html")

@app.route('/profile')
def index():
    return render_template("profile.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

