--Creación USUARIO
INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
VALUES ('Nicoffee','1234',NOW());

--Creacion ESTUDIANTE
INSERT INTO PUBLIC."ESTUDIANTE" (usu_id,est_tipo,est_exp_total)
VALUES ('Nicoffee','free',9999);

--Creacion DEFINICION
INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional)
VALUES ('get-d1s7:Nicooffeees0','agarrar','es','',FALSE,FALSE);

--Creacion REVISION
INSERT INTO PUBLIC."REVISION" (rev_id,rev_es_correcta,rev_nivel_srs)
VALUES ('get-d1s5:NicooffeeFR0',TRUE,1);

--Creación PALABRA
INSERT INTO PUBLIC."PALABRA" (pal_id,pal_tipo,pal_es_ofensiva)
VALUES ('get-d1s7:Nicooffee','transitive verb',FALSE);

--Creación PALABRA_DEFINICION
INSERT INTO PUBLIC."PALABRA_DEFINICION" (pal_id,def_id)
VALUES ('get-d1s7:Nicooffee','get-d1s7:Nicooffeees0');

--Creación FLASHCARD
INSERT INTO PUBLIC."FLASHCARD" (fla_id,fla_tipo,fla_nivel_srs)
VALUES ('get-d1s7:NicoffeeFR','reco','1')
ON CONFLICT (fla_id) DO UPDATE
SET fla_nivel_srs = excluded.fla_nivel_srs;

--Creación FLASHCARD_REVISION
INSERT INTO PUBLIC."FLASHCARD_REVISION" (rev_id,fla_id,rev_fla_fecha)
VALUES ('go:1-d1s104NicoffeeFP0','go:1-d1s104NicoffeeFP',NOW())
ON CONFLICT ON CONSTRAINT "PK_FLA_REV" DO NOTHING;

--Creación USUARIO_PALABRA
INSERT INTO PUBLIC."USUARIO_PALABRA" (usu_id,pal_id)
VALUES ('Nicoffee','get-d1s7:Nicooffee');

--Creación USU_PAL_FLASHCARD
INSERT INTO PUBLIC."USU_PAL_FLASHCARD" (usu_id,pal_id,fla_id,fla_fecha_creacion)
VALUES ('Nicoffee','go:1-d1s1','go:1-d1s1NicoffeeFR',NOW());

--Creación USU_PAL_DEFINICION
INSERT INTO PUBLIC."USU_PAL_DEFINICION" (usu_id,pal_id,def_id,def_principal,def_extra)
VALUES ('Nicoffee','go:1-d1s1:Nicooffee','go:1-d1s1:Nicooffeeen0',TRUE,FALSE);