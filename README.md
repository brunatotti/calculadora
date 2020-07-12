# Calculadora
Projeto web de uma calculadora

## Build
- Instalar máquina virtual
<pre>pip install virtualenv</pre>

- Criar máquina virtual
<pre>python -m venv venv</pre>

- Ativar máquina vitual
<pre>cd venv</pre>
<pre>cd Scripts</pre>
<pre>activate</pre>

- Clonar projeto no nível da pasta venv
<pre>git clone https://github.com/brunatotti/calculadora</pre>
<pre>cd calculadora</pre>

- Instalação dos pacotes/libs necessários
<pre>pip install -r requirements.txt</pre>

- Rodar projeto
<pre>python -m flask run</pre>

## Estrutura do projeto
<pre>Controllers
    __init__.py
    autenticacao.py
    calculadora.py
    historico.py
Models
    __init__.py
    calculadora.py
    user.py
Statics 
    css
    img
    js
Templates
    .html
__init__.py
.gitignore
app.py
README.md
requirements.txt</pre>

### Modelo MVC (Model View Controller)
#### Model
- Em <b>Models</b> constam as tabelas criadas. O que é feito no controller resultará na manipulação do banco de bados. 

#### View
- Em <b>View</b> os repositórios são: <b>Static e Template</b>;
- Em <b>Static</b> constam os arquivos estáticos (css, img e js);
- Em <b>Templates</b> constam as páginas html.

#### Controller
- Em <b>Controllers</b> consta toda a lógica (Direcionamento das páginas, o que ocorre ao clicar)

## Banco de Dados
-Para a criação do banco de dados foi usado o <b>ORM SQLALCHEMY</b>. É uma ferramenta utilizada para facilitar a criação e comunicação com o banco de dados;
- Toda configuração necessária consta no arquivo app.py

<pre>
#Banco de dados
db_path = os.path.dirname(os.path.abspath(__file__))
#Caminho do arquivo banco de dados
db_file = "sqlite:///calculadora.db"
app.config["SQLALCHEMY_DATABASE_URI"] = db_file

app.config['SECRET_KEY'] = 'sifghfiuasasdkmlkfmg23165'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Instância do SQLAlchemy
db = SQLAlchemy(app)
</pre>

##### Ordem do que foi feito
- Criação da máquina virtual (python3 -m venv cacluladora);
- Criação do projeto;
- Organização das pastas MVC;
- Instalação do requirements.txt (Flask e Jinja: pip install -r requirements.txt);
- Criação das páginas html;
- Criação dos estilos com css e bootstrap;
- Criação dos vínculos entre as páginas;
- Criação do arquivo .gitignore;
- Criação do banco de dados;
- Criação da lógica para a calculadora;
- Revisão.
