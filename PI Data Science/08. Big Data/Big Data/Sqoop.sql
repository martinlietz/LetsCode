--Em um terminal, acesse o mysql pelo comando: 
mysql -uroot -pcloudera 

--Listar databases: 
SHOW databases;

--Criar um Database
CREATE DATABASE letscode;

--Selecionar Database
USE letscode;

--Listar tabelas de um database: 
SHOW TABLES from letscode;

--CRIAR TABELA
CREATE TABLE cliente(id int, nome varchar(100));

--inserir registros teste
INSERT INTO cliente VALUES ((1, Maria),(2, Joao));
