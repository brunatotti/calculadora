from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from datetime import datetime

from ..models import Calculadora
from ..app import db

#Declaração blueprint
module = Blueprint("historico", __name__)

#Rota da página
@module.route("/historico", methods=["GET","POST"])
@login_required
def get_historico():
    if request.method == "GET":
        calculos = Calculadora.query.all()
        calculos = calculos[::-1]
        return render_template('historico.html', calculos = calculos)
        