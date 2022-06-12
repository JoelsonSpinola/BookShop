#executar e instal as seguintes bibliotecas:
#obs: coamndos descritos para distros linux a pricipio, em caso de windows pode variar
#pip install pymysql
#pip install marshmallow-sqlalchemy
#pip install flask-marshmallow
#pip install flask-sqlalchemy
#pip install flask

#bibliotecas importadas
from crypt import methods
from unicodedata import category
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#criar a base de dados com o mysql workbench com o nome de livraria
app = Flask(__name__)#instanciar aplicacao
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<passworfromroot>@localhost:3306/Livraria'#configurar a conexao com o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

db=SQLAlchemy(app)#instanciar o banco de dados
ma=Marshmallow(app)#instanciar o marshmallow

#criar a classe livro
class Livro(db.Model):#criar a classe livro
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), unique=True)
    autor = db.Column(db.String(100))
    isbn = db.Column(db.Integer)
    genero = db.Column(db.String(100))
    preco = db.Column(db.Float)
    #criar o construtor
    def __init__(self, titulo, autor, isbn, genero, preco):#construtor
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.preco = preco

db.create_all()#criar a tabela
#os valores da tabela sao adicionados pelo mysql workbench
#criar o esquema
class LivroSchema(ma.Schema):   #criar o esquema
    class Meta: #criar o meta
        fields = ('id','titulo','autor','isbn','genero','preco')    #criar o campo

#apenas um valor
category_schema=LivroSchema()
#varios valores
category_schema=LivroSchema(many=True)  

if __name__ == "__main__":  #inicia a aplicacao
    app.run(debug=True)#inicia a aplicacao
