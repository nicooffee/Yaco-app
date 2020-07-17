--Existe registro de usuarios en USUARIO_PALABRA x palabra
SELECT EXISTS(SELECT 1 FROM PUBLIC."USUARIO_PALABRA" WHERE pal_id = 'go:1-d1s2:es00');