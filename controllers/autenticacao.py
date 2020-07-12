from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from ..models import User
from ..app import db

#Declaração blueprint
module = Blueprint('autenticacao', __name__)

#Rota da página
@module.route("/", methods=["GET","POST"])
def main():
    return redirect(url_for('autenticacao.login'))

#Rota da página
@module.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email nao encontrado!')
            return redirect(url_for('autenticacao.login'))
        elif not check_password_hash(user.password,password):
            flash('Senha incorreta')
            return redirect(url_for('autenticacao.login'))
        login_user(user)
        return redirect(url_for('calculadora.calculo'))

#Rota da página
@module.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "GET":
        return render_template('cadastro.html')
    elif request.method == "POST":
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(user_name=user_name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('autenticacao.login'))

#Rota da página
@module.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('autenticacao.login'))
