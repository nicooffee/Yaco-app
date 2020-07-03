--Creación usuario
INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
VALUES ('Nicoffee','1234',NOW());

INSERT INTO PUBLIC."ESTUDIANTE" (usu_id,est_tipo)
VALUES ('Nicoffee','free');

--Creacion definicion
INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra)
VALUES ('get-d1s5:Nicoffee-d1','tomar','es','(un tren, etc.)',FALSE,FALSE);