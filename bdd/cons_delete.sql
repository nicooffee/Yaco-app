--eliminar USUARIO
DELETE from PUBLIC."USUARIO" WHERE usu_id = 'Nicoffee';
--eliminar DEFINICION
DELETE from PUBLIC."DEFINICION" WHERE def_id = 'get-d1s5:Nicoffee1';
--eliminar REVISION
DELETE from PUBLIC."REVISION" WHERE rev_id = 'get-d1s5:NicoffeeFR0';
--eliminar PALABRA
DELETE from PUBLIC."PALABRA" WHERE pal_id = 'get-d1s7:Nicooffee';
--eliminar FLASHCARD
DELETE from PUBLIC."FLASHCARD" WHERE fla_id = 'get-d1s7:NicoffeeFR';

DELETE FROM PUBLIC."USUARIO_PALABRA" WHERE usu_id = 'Nicoffee' AND pal_id = 'get-d1s7:Nicooffee';