from FlashcardList import FlashcardList
from PalabraDict import PalabraDict
from Flashcard import Flashcard
from Palabra import Palabra
from database.Database import PSConnection
from interface.DBWriter import DBWriter
import datetime
class Usuario(DBWriter):
    def __init__(
            self,
            id,
            flashcard_list = FlashcardList(),
            palabra_dict = PalabraDict(),
            fecha_registro = datetime.datetime.now(),
            ultimo_logeo = datetime.datetime.now()):
        self.id = id
        self.flashcard_list = flashcard_list
        self.palabra_dict   = palabra_dict 
        self.fecha_registro = fecha_registro
        self.ultimo_logeo   = ultimo_logeo
    #
    #
    #
    #
    #
    #input: elemento de un desglose
    #output: palabra agregada
    def agregar_palabra(self,palabra_info):
        P = self.palabra_dict.agregar_palabra(palabra_info,self.id)
        if P is not None:
            P.add_data()
            psc = PSConnection()
            psql_query_up = """INSERT INTO PUBLIC."USUARIO_PALABRA" (usu_id,pal_id) VALUES (%s,%s);"""
            psql_query_f = """INSERT INTO PUBLIC."USU_PAL_FLASHCARD" (usu_id,pal_id,fla_id,fla_fecha_creacion) VALUES (%s,%s,%s,%s);"""
            psql_query_d = """INSERT INTO PUBLIC."USU_PAL_DEFINICION" (usu_id,pal_id,def_id,def_principal,def_extra) VALUES (%s,%s,%s,%s,%s)"""
            up_data = (self.id,P.get_id())
            psc.query(psql_query_up,up_data)
            for f in P.get_flashcard_list():
                self.flashcard_list.agregar_flashcard(f)
                f.add_data()
            f_data = map(lambda x: (self.id,P.get_id(),x.get_id(),x.get_fecha_creacion()),P.get_flashcard_list())
            def_0 = P.get_definicion_iter(Palabra.lang[0])
            def_1 = P.get_definicion_iter(Palabra.lang[1])
            d_id_0 = map(lambda x: (self.id,P.get_id(),x.get_id(),x.get_es_principal(),x.get_es_extra()),def_0)
            d_id_1 = map(lambda x: (self.id,P.get_id(),x.get_id(),x.get_es_principal(),x.get_es_extra()),def_1)
            psc.query_many(psql_query_f,f_data)
            psc.query_many(psql_query_d,d_id_0)
            psc.query_many(psql_query_d,d_id_1)
        return P
    #
    #
    #
    #
    #
    #input: id de una palabra (de los del desglose)
    #output: palabra eliminada
    def eliminar_palabra(self,id):
        P = self.palabra_dict.eliminar_palabra(id)
        if P is not None:
            psc = PSConnection()
            psql_query_up  = """DELETE FROM PUBLIC."USUARIO_PALABRA" WHERE usu_id = (%s) AND pal_id = (%s)"""
            psql_query_up2 = """SELECT EXISTS(SELECT 1 FROM PUBLIC."USUARIO_PALABRA" WHERE pal_id = (%s))"""
            data_up = (self.id,P.get_id())
            psc.query(psql_query_up,data_up)
            data_up2 = (P.get_id(),)
            res = psc.fetch_one(psql_query_up2,data_up2)
            if res[0]:
                def_extra = P.get_def_extra()
                def_extra.del_data()
            else:
                P.del_data()
            for F_p in P.get_flashcard_list(): 
                F = self.flashcard_list.eliminar_flashcard(F_p.get_id())
                F_p.del_data()
        return P
            

    #GETTER###################################
    def get_id(self):
        return self.id
    def get_fecha_registro(self):
        return fecha_registro
    def get_ultimo_logeo(self):
        return ultimo_logeo
    #SETTER###################################
    def set_id(self,id):
        self.id = id
    def set_fecha_registro(self,fecha_registro):
        self.fecha_registro = fecha_registro
    def set_ultimo_logeo(self,ultimo_logeo):
        self.ultimo_logeo = ultimo_logeo
    #DB#######################################
    def del_data(self,*arg):
        psql_query = 'DELETE from PUBLIC."USUARIO" WHERE usu_id = %s;'
        psc = PSConnection()
        data = (self.id,)
        return psc.query(psql_query,data)

if __name__ == "__main__":
    pass