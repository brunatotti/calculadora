from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from datetime import datetime

from ..models import Calculadora
from ..app import db

#Declaração blueprint
module = Blueprint("calculadora", __name__)

#Rota da página
@module.route("/calculadora", methods=["GET","POST"])
@login_required
def calculo():
    if request.method == "GET":
        return render_template('calculadora.html')
    elif request.method =="POST":
        num_1 = request.form.get("num_1")
        operador = request.form.get("operador")
        num_2 = request.form.get("num_2")
        resposta = operacao(num_1,operador,num_2)

        #Guardar informações para apresentar no histórico
        novo_calculo = Calculadora(expressao=resposta, created = datetime.now(), user_name=current_user.user_name)
        db.session.add(novo_calculo)
        db.session.commit()
        return render_template('calculadora.html', resposta = resposta[resposta.find('=')+1:-2])

#Lógica da aplicação (soma, subtração, multiplicação, divisão, potenciação e radiciação)
def operacao(num_1,op,num_2):
    if op == "soma":
        exp = str(num_1)+" + "+str(num_2) + " = " + str(float(num_1)+float(num_2))
    elif op == "subtrai":
        exp = str(num_1)+" - "+str(num_2) + " = " + str(float(num_1)-float(num_2))
    elif op == "multiplica":
        exp = str(num_1)+" * "+str(num_2) + " = " + str(float(num_1)*float(num_2))
    elif op == "divide":
        if num_2 == str('0'):
            exp = 'Erro, divisão por ZERO'
        else:
            exp = str(num_1)+" / "+str(num_2) + " = " + str(float(num_1)/float(num_2))
    elif op == "potencia":
            exp = str(num_1)+" ** "+str(num_2) + " = " + str(float(num_1)**float(num_2))
    elif op == "raiz":
            exp = str(num_1)+" ** "+str(num_2) + " = " + str(float(num_1)**(1/float(num_2)))
    return exp
