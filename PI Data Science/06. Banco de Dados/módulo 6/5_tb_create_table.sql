-- PK simples
SELECT tb_estados.*, tb_cidades.nome, tb_cidades.idEstado
FROM tb_estados
INNER JOIN tb_cidades ON tb_estados.id = tb_cidades.idEstado;

CREATE TABLE tb_estados (
	id SERIAL,
	uf VARCHAR(2) NOT NULL,
	nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE tb_cidades (
	id SERIAL,
	nome VARCHAR(50) NOT NULL,
	idEstado INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (idEstado) REFERENCES tb_estados (id)
);

DELETE FROM tb_estados WHERE id = 7;
