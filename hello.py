#!/bin/bash
#'flask' is a library anf Flask is a class inside the library.
from flask import Flask, render_template
print("hello")
# For our web aplication to run an instance of the Flask class has to be created
app = Flask(__name__)
# URL of the webbrowser
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/child/')
def child():
	return render_template('child.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

#script currently running always have the name "__main__"

