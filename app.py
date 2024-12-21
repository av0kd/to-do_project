from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    return render_template('adicionar.html')