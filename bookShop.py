#bibliotecas importadas
from http.cookies import BaseCookie
from flask import Flask, jsonify, request
from crypt import methods
from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from cd_dvd import CD_DVD
from cd_dvd import  category_schema_cd
from cd_dvd import CD_DVD_Schema
from livros import Livro
from livros import  category_schema
from livros import LivroSchema

app=Flask(__name__)#instanciar aplicacao
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<PasswordfromRoot>@localhost:3306/Livraria'#configurar a conexao com o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#instanciar o banco de dados
db=SQLAlchemy(app)#instanciar o banco de dados


#Insirir um livro
@app.route('/livros/add', methods=['POST'])#criar a rota
def add_livro():#criar a funcao
    titulo = request.json['titulo']#pegar o titulo do json
    autor = request.json['autor']#pegar o autor do json
    isbn = request.json['isbn']#pegar o isbn do json
    genero = request.json['genero']#pegar o genero do json
    preco = request.json['preco']#pegar o preco do json
    new_livro = Livro(titulo, autor, isbn, genero, preco)#criar um novo livro
    db.session.add(new_livro)#adicionar o livro ao banco de dados
    db.session.commit()#commitar o banco de dados
    return jsonify('Livro adicionado com sucesso!')#retornar a mensagem
#Get all livros
@app.route('/livros', methods=['GET'])#criar a rota
def get_livros():   #criar a funcao
    livros = Livro.query.all()#pegar todos os livros
    result = category_schema.dump(livros)   #serializar os livros
    return jsonify(result)  #retornar os livros

#Get autor - lista os livros de um autor
@app.route('/livros/<string:autor>', methods=['GET'])   #criar a rota
def get_livros_autor(autor):    #criar a funcao
    livros = Livro.query.filter_by(autor=autor).all()   #pegar todos os livros de um autor
    result = category_schema.dump(livros)   #serializar os livros
    return jsonify(result)  #retornar os livros
#get livro menor preco
@app.route('/livros/preco/menor', methods=['GET'])  #criar a rota
def get_livros_preco():  #criar a funcao
    livros = Livro.query.order_by(Livro.preco).all()    #pegar todos os livros de um autor
    result = category_schema.dump(livros)[0]    #serializar os livros
    return jsonify(result)  #retornar os livros
#get livro maior preco
@app.route('/livros/preco/maior', methods=['GET'])  #criar a rota
def get_livros_preco_maior():   #criar a funcao
    livros = Livro.query.order_by(Livro.preco.desc()).all() #pegar todos os livros de um autor
    result = category_schema.dump(livros)[0]    #serializar os livros
    return jsonify(result)  #retornar os livros
#get total de livros
@app.route('/livros/total', methods=['GET'])    #criar a rota
def get_livros_total():  #criar a funcao
    livros = Livro.query.count()    #pegar todos os livros de um autor
    return jsonify({"Total de livros =":livros})    #retornar os livros
#eliminar livro de um autro
@app.route('/livros/<string:autor>', methods=['DELETE'])    #criar a rota
def delete_livros_autor(autor): #criar a funcao
    livros = Livro.query.filter_by(autor=autor).delete()    #pegar todos os livros de um autor
    db.session.commit()  #commitar o banco de dados
    return jsonify('Livro eliminado')   #retornar os livros

#Insirir um CD_DVD
@app.route('/CD_DVD/add', methods=['POST']) #criar a rota
def add_cd_dvd():   #criar a funcao
    tituloAlbum = request.json['tituloAlbum']   #pegar o titulo do json
    artista = request.json['artista']   #pegar o artista do json
    ano = request.json['ano']   #pegar o ano do json
    genero = request.json['genero']  #pegar o genero do json
    NumeroDisco = request.json['NumeroDisco']   #pegar o NumeroDisco do json
    duracao = request.json['duracao']   #pegar o duracao do json
    preco = request.json['preco']   #pegar o preco do json
    new_cd_dvd = CD_DVD(tituloAlbum, artista, ano, genero, NumeroDisco, duracao, preco)  #criar um novo CD_DVD
    db.session.add(new_cd_dvd)  #adicionar o CD_DVD ao banco de dados
    db.session.commit() #commitar o banco de dados
    return jsonify('novo CD_DVD adicionado')    #retornar a mensagem

#Get all CD_DVD
@app.route('/CD_DVD', methods=['GET'])  #criar a rota
def get_CD_DVD():   #criar a funcao
    cd_dvd = CD_DVD.query.all() #pegar todos os CD_DVD
    result = category_schema_cd.dump(cd_dvd)    #serializar os CD_DVD
    return jsonify(result)  #retornar os CD_DVD

#Get artista - lista os CD_DVD de um artista
@app.route('/CD_DVD/<string:artista>', methods=['GET'])  #criar a rota
def get_CD_DVD_artista(artista):    #criar a funcao
    cd_dvd = CD_DVD.query.filter_by(artista=artista).all()  #pegar todos os CD_DVD de um artista
    result = category_schema_cd.dump(cd_dvd)    #serializar os CD_DVD
    return jsonify(result)  #retornar os CD_DVD
#Get CD_DVD menor preco
@app.route('/CD_DVD/preco/menor', methods=['GET'])  #criar a rota
def get_CD_DVD_preco(): #criar a funcao
    cd_dvd = CD_DVD.query.order_by(CD_DVD.preco).all()  #pegar todos os CD_DVD de um artista
    result = category_schema_cd.dump(cd_dvd)[0]   #serializar os CD_DVD
    return jsonify(result)  #retornar os CD_DVD
#Get CD_DVD maior preco
@app.route('/CD_DVD/preco/maior', methods=['GET'])  #criar a rota
def get_CD_DVD_preco_maior():   #criar a funcao
    cd_dvd = CD_DVD.query.order_by(CD_DVD.preco.desc()).all()   #pegar todos os CD_DVD de um artista
    result = category_schema_cd.dump(cd_dvd)[0]  #serializar os CD_DVD
    return jsonify(result)  #retornar os CD_DVD

#Get Total de CD_DVD
@app.route('/CD_DVD/total', methods=['GET'])    #criar a rota
def get_CD_DVD_total(): #criar a funcao
    cd_dvd = CD_DVD.query.count()   #pegar todos os CD_DVD de um artista
    return jsonify(cd_dvd)  #retornar os CD_DVD

#DELETE CD_DVD de um artista
@app.route('/CD_DVD/delete/<string:artista>', methods=['DELETE'])   #criar a rota
def delete_CD_DVD_artista(artista): #criar a funcao
    cd_dvd = CD_DVD.query.filter_by(artista=artista).delete()   #pegar todos os CD_DVD de um artista
    db.session.commit() #commitar o banco de dados
    return jsonify('CD_DVD Deleted')    #retornar os CD_DVD

#listar livros e CD_DVD de um determinado autor/artista
@app.route('/livros_CD_DVD/<string:autor>', methods=['GET'])    #criar a rota
def get_livros_CD_DVD_autor(autor): #criar a funcao
    livros = Livro.query.filter_by(autor=autor).all()   #pegar todos os livros de um autor
    cd_dvd = CD_DVD.query.filter_by(artista=autor).all()    #pegar todos os CD_DVD de um artista
    result = category_schema.dump(livros)   #serializar os livros
    result_cd = category_schema_cd.dump(cd_dvd)  #serializar os CD_DVD
    return jsonify(result+result_cd)    #retornar os livros



if __name__ == "__main__":  #executar o programa
     app.run(host="0.0.0.0",port=5000, debug=True)#inicia a aplicacao
