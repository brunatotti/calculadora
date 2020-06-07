from flask import Flask
from flask.templating import render_template

app = Flask (__name__)

@app.route("/", methods = ['GET'])
@app.route ("/login", methods = ['GET'])
@app.route ("/bruna", methods = ['GET'])
def login ():
     return render_template('login.html')

@app.route("/cadastro", methods = ['GET'])
def cadastro ():
    return render_template('cadastro.html')

@app.route("/index", methods = ['GET'])
def index ():
    return render_template('index.html')

@app.route("/historico", methods = ['GET'])
def historico ():
    return render_template('historico.html')
