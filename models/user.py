from calculadora.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#Criação da tabela User
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    #Criação das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), index=False, unique=False,nullable=False)
    email = db.Column(db.String(80),index=True,unique=True,nullable=False)
    password = db.Column(db.String(200),primary_key=False,unique=False,nullable=False)
