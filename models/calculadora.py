from calculadora.app import db
from . import User

#Criação da tabela Calculadora
class Calculadora(db.Model):
    __tablename__ = 'calculadora'

    #Criação das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    expressao = db.Column(db.String(100), index=False, unique=False,nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    user_name = db.Column(db.String(100), index=False, unique=False,nullable=False)
