#bibliotecas necessarias:
from crypt import methods
from unicodedata import category
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#criar a base de dados com o mysql workbench com o nome de livraria
app = Flask(__name__)#instanciar aplicacao
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:AlucarD20@localhost:3306/Livraria'#configurar a conexao com o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)#instanciar o banco de dados
ma=Marshmallow(app)#instanciar o marshmallow


#criar a classe dvd#############################################
class CD_DVD(db.Model):#criar a classe CD_DVD
    id = db.Column(db.Integer, primary_key=True)
    tituloAlbum = db.Column(db.String(100), unique=True)
    artista = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    genero = db.Column(db.String(100))
    NumeroDisco = db.Column(db.Integer)
    duracao = db.Column(db.Integer)
    preco = db.Column(db.Float)
    
    #criar o construtor
    def __init__(self, tituloAlbum, artista, ano, genero, NumeroDisco, duracao, preco):#construtor
        self.tituloAlbum = tituloAlbum
        self.artista = artista
        self.ano = ano
        self.genero = genero
        self.NumeroDisco = NumeroDisco
        self.duracao = duracao
        self.preco = preco
db.create_all()#criar a tabela
#os valores da tabela sao adicionados pelo mysql workbench
#criar o esquema
class CD_DVD_Schema(ma.Schema): #criar o esquema
    class Meta: #criar o meta
        fields = ('id','tituloAlbum','artista','ano','genero','NumeroDisco','duracao','preco')  #criar o campo


#apenas um valor
category_schema_cd=CD_DVD_Schema()  
#varios valores
category_schema_cd=CD_DVD_Schema(many=True)


if __name__ == "__main__":  #inicia a aplicacao
    app.run(debug=True)#inicia a aplicacao