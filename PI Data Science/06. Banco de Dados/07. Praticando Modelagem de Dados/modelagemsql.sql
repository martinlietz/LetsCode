--CREATE DATABASE livraria;


CREATE TABLE tb_cliente (
    idCliente SERIAL,
    cpf INT NOT NULL,
    nome VARCHAR(250) NOT NULL,
    endereco VARCHAR(1000) NOT NULL,
    telefone VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL,
    PRIMARY KEY (idCliente)
);

CREATE TABLE tb_editor (
    id SERIAL,
    nome VARCHAR(50) NOT NULL,
    idEstado INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE tb_livro (
    isbn INT NOT NULL,
    titulo VARCHAR(250) NOT NULL,
    categoria VARCHAR(250) NOT NULL,
    ano_publicacao INT NOT NULL,
    idEditor INT NOT NULL,
    estoque INT NOT NULL,
    autores VARCHAR(500) NOT NULL,
    PRIMARY KEY (isbn),
    CONSTRAINT fk_editor FOREIGN KEY (idEditor) REFERENCES tb_editor (id)
);


CREATE TABLE tb_livros_Clientes (
    idCliente INT NOT NULL,
    isbn INT NOT NULL,
    PRIMARY KEY (idCliente, isbn),
    CONSTRAINT fk_cliente FOREIGN KEY (idCliente) REFERENCES tb_cliente (idCliente),
    CONSTRAINT fk_livro FOREIGN KEY (isbn) REFERENCES tb_livro (isbn)
);

DROP TABLE tb_livros_Clientes;
DROP TABLE tb_livro;
DROP TABLE tb_editor;
DROP TABLE tb_cliente;