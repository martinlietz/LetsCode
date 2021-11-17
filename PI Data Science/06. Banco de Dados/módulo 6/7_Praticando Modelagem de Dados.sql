--DATABASE
CREATE DATABASE bd_livraria;

--TABLES
CREATE TABLE tb_cliente(
id_cliente SERIAL NOT NULL,
cpf CHAR(11) NOT NULL,
nome VARCHAR(50) NOT NULL,
endereco VARCHAR(50) NOT NULL,
tel INT NOT NULL,
email VARCHAR(30) NOT NULL,
PRIMARY KEY(id_cliente));

CREATE TABLE tb_editora(
id_editora SERIAL NOT NULL,
nome VARCHAR(50) NOT NULL,
email VARCHAR(30) NOT NULL,
tel INT NOT NULL,
cel INT NOT NULL,
PRIMARY KEY(id_editora));

CREATE TABLE tb_livro(
id_livro SERIAL NOT NULL,
titulo VARCHAR(60) NOT NULL,
categoria VARCHAR(50) NOT NULL,
isbn CHAR(13) NOT NULL,
ano CHAR(4) NOT NULL,
editora INT NOT NULL,
autor VARCHAR(50) NOT NULL,
PRIMARY KEY(id_livro),
FOREIGN KEY(editora) REFERENCES tb_editora(id_editora));

CREATE TABLE tb_estoque(
id_estoque SERIAL NOT NULL,
qtde INT NOT NULL,
livro INT NOT NULL,
preco NUMERIC (16,2),
PRIMARY KEY(id_estoque),
FOREIGN KEY(livro) REFERENCES tb_livro(id_livro));

--INSERT
INSERT INTO tb_cliente (cpf,nome,endereco,tel,email) VALUES 
(1021031049,'Kamila Peres','Rua Pensilvania','1135354747','kamila.peres@outlook.com');

INSERT INTO tb_editora (nome,email,tel,cel) VALUES 
('Companhia Editora Nacional','cen@otlook.com','1845355757','1135354747');

INSERT INTO tb_livro (titulo,categoria,isbn,ano,editora,autor) VALUES 
('Como Fazer Amigos E Influenciar Pessoas','Auto Ajuda','1-4391-6734-6',2012, 01, 'Dale Carnegie');

INSERT INTO tb_estoque (qtde,livro,preco) VALUES (20,01,50.02);