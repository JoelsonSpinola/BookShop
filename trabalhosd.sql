create database if not exists Livraria;

use Livraria;

insert into livro(id,titulo,autor,isbn,genero,preco) 
value(1,"AI","Kenny Afonso",0001,"Cientifico","5000"),
(2,"React","Jspinola",0002,"WEB delop","3000"),
(3,"Python","Astro",0003,"Cientifico","1000"),
(4,"AI VOL2","Kenny Afonso",0004,"Cientifico","6000");


insert into CD_DVD(id,tituloAlbum,artista,ano,genero,NumeroDisco,duracao,preco)
value
(1,"5AM","Mark Delman",2016,"RAP",0001,40,1000),
(2,"Fortunas do Thug","Kiddye Bonz",2015,"RAP",0002,60,1500),
(3,"Music to Be Murdered By","Eminem",2020,"RAP",0003,70,2000),
(4,"Vida de um Estudante","Kenny Afonso",2022,"Acustic",0004,"40","200");
