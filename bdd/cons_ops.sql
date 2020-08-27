SELECT PUBLIC."USUARIO".usu_id,est_tipo,usu_fecha_registro,est_exp_total
FROM PUBLIC."USUARIO"
INNER JOIN PUBLIC."ESTUDIANTE" ON PUBLIC."USUARIO".usu_id = PUBLIC."ESTUDIANTE".usu_id
WHERE PUBLIC."USUARIO".usu_id = 'Nicoffee';

--Existe registro de usuarios en USUARIO_PALABRA x palabra
SELECT EXISTS(SELECT 1 FROM PUBLIC."USUARIO_PALABRA" WHERE pal_id = 'go:1-d1s2:es00');
--Existe usuario registrado
SELECT EXISTS(SELECT 1 FROM PUBLIC."USUARIO" WHERE usu_id = 'Nicoffee');
--Todas las palabras de un usuario
SELECT PUBLIC."PALABRA".pal_id,pal_tipo,pal_es_ofensiva 
FROM PUBLIC."PALABRA"
INNER JOIN PUBLIC."USUARIO_PALABRA" ON PUBLIC."PALABRA".pal_id = PUBLIC."USUARIO_PALABRA".pal_id
WHERE PUBLIC."USUARIO_PALABRA".usu_id = 'Nicoffee';

--Todas las palabras de un usuario con sus dos flashcard
SELECT PUBLIC."PALABRA".pal_id,pal_tipo,pal_es_ofensiva,PUBLIC."FLASHCARD".fla_id,fla_fecha_creacion,fla_nivel_srs,fla_tipo
FROM PUBLIC."PALABRA"
INNER JOIN PUBLIC."USU_PAL_FLASHCARD" ON PUBLIC."PALABRA".pal_id = PUBLIC."USU_PAL_FLASHCARD".pal_id
INNER JOIN PUBLIC."FLASHCARD" ON PUBLIC."USU_PAL_FLASHCARD".fla_id = PUBLIC."FLASHCARD".fla_id
WHERE PUBLIC."USU_PAL_FLASHCARD".usu_id = 'Nicoffee'
ORDER BY PUBLIC."PALABRA".pal_id ASC;

--Flashcards de un usuario para una palabra
SELECT PUBLIC."FLASHCARD".fla_id,fla_fecha_creacion,fla_nivel_srs,fla_tipo 
FROM PUBLIC."FLASHCARD"
INNER JOIN PUBLIC."USU_PAL_FLASHCARD" ON PUBLIC."FLASHCARD".fla_id = PUBLIC."USU_PAL_FLASHCARD".fla_id
WHERE usu_id = 'Nicoffee' AND pal_id = 'go:1-d1s18';

--Revisiones para una flashcard
SELECT PUBLIC."REVISION".rev_id,rev_fla_fecha,rev_nivel_srs,rev_es_correcta
FROM PUBLIC."REVISION"
INNER JOIN PUBLIC."FLASHCARD_REVISION" ON PUBLIC."REVISION".rev_id = PUBLIC."FLASHCARD_REVISION".rev_id
WHERE fla_id = 'go:1-d1s18NicoffeeFR'
ORDER BY rev_fla_fecha DESC;

--Definiciones de una palabra, para un usuario
SELECT PUBLIC."DEFINICION".def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra
FROM PUBLIC."DEFINICION"
INNER JOIN PUBLIC."USU_PAL_DEFINICION" ON PUBLIC."DEFINICION".def_id = PUBLIC."USU_PAL_DEFINICION".def_id
WHERE usu_id = 'Nicoffee' AND pal_id = 'go:1-d1s18';

--Definiciones de una palabra, para un usuario, con idioma específico
SELECT PUBLIC."DEFINICION".def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra
FROM PUBLIC."DEFINICION"
INNER JOIN PUBLIC."USU_PAL_DEFINICION" ON PUBLIC."DEFINICION".def_id = PUBLIC."USU_PAL_DEFINICION".def_id
WHERE usu_id = 'Nicoffee' AND pal_id = 'go:1-d1s18' AND def_idioma = 'en';

--Seleccionar contraseña
SELECT usu_pass FROM PUBLIC."USUARIO" WHERE usu_id = 'Nicoffee';