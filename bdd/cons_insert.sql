--Creación usuario
INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
VALUES ('Nicoffee','1234',NOW());

INSERT INTO PUBLIC."ESTUDIANTE" (usu_id,est_tipo)
VALUES ('Nicoffee','free');