from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

#Variavel que controla a aplicação toda
app = Flask(__name__)

#Banco de dados
db_path = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///calculadora.db"
app.config["SQLALCHEMY_DATABASE_URI"] = db_file
app.config['SECRET_KEY'] = 'sifghfiuasasdkmlkfmg23165'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Instância do SQLAlchemy
db = SQLAlchemy(app)

#Login da aplicação
login_manager = LoginManager()
login_manager.login_view = 'autenticacao.login'
login_manager.init_app(app)

from .models import User
from .models import Calculadora

#Criar banco de dados (tabelas)
db.create_all(app=app)

#Logar
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .controllers import autenticacao as autenticacao_bp
app.register_blueprint(autenticacao_bp)

from .controllers import calculadora as calculadora_bp
app.register_blueprint(calculadora_bp)

from .controllers import historico as historico_bp
app.register_blueprint(historico_bp)

#Segurança para executar o arquivo principal
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='5000')
    