--Creación USUARIO
INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
VALUES ('Nicoffee','1234',NOW());

--Creacion ESTUDIANTE
INSERT INTO PUBLIC."ESTUDIANTE" (usu_id,est_tipo)
VALUES ('Nicoffee','free');

--Creacion DEFINICION
INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra)
VALUES ('get-d1s7:Nicooffeees0','agarrar','es','',FALSE,FALSE);

--Creacion REVISION
INSERT INTO PUBLIC."REVISION" (rev_id,rev_es_completa,rev_equivocacion_previa,rev_nivel_srs)
VALUES ('get-d1s5:NicooffeeFR0',TRUE,TRUE,1);

--Creación PALABRA
INSERT INTO PUBLIC."PALABRA" (pal_id,pal_tipo,pal_es_ofensiva)
VALUES ('get-d1s7:Nicooffee','transitive verb',FALSE);

--Creación PALABRA_DEFINICION
INSERT INTO PUBLIC."PALABRA_DEFINICION" (pal_id,def_id)
VALUES ('get-d1s7:Nicooffee','get-d1s7:Nicooffeees0');

--Creación FLASHCARD
INSERT INTO PUBLIC."FLASHCARD" (fla_id,fla_tipo,fla_nivel_srs)
VALUES ('get-d1s7:NicooffeeFR','reco','1');