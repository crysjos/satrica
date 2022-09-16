from os import truncate
from pickle import TRUE
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contribuyente')
def contribuyente():
    return render_template('contribuyente.html')

if __name__ == '__main__':
    app.run(debug=TRUE)
    