from RevisionList import RevisionList
from datetime import datetime,timedelta
from config import config
from interface.DBWriter import DBWriter
from database.Database import PSConnection
class Flashcard(DBWriter):
    def __init__(
            self,
            id, 
            palabra,
            tipo, #reco, prod
            fecha_creacion,
            revision_list,
            nivel_srs = 1):
        self.id = id
        self.palabra = palabra
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.nivel_srs = nivel_srs
        self.revision_list = revision_list
    #
    #
    #
    #
    #
    def completar_revision(self,es_correcta,fecha = datetime.now()):
        R = self.revision_list.completar_revision(self.id,fecha,es_correcta,self.nivel_srs)
        self.nivel_srs = self.nivel_srs + (1 if es_correcta else (-1 if self.nivel_srs>1 else 0))
        return R
    #
    #
    #
    #
    #

    #GETTER###################################
    def get_id(self):
        return self.id
    def get_tipo(self):
        return self.tipo
    def get_palabra(self):
        return self.palabra
    def get_fecha_creacion(self):
        return self.fecha_creacion
    def get_nivel_srs(self):
        return self.nivel_srs
    def get_fecha_sig(self):
        rev_list = self.revision_list
        nivl_srs = self.nivel_srs
        F = rev_list.get_fecha_ult_rev()
        if F is None:
            return self.get_fecha_creacion() + timedelta(seconds=config.get_srs_time(1))
        else:
            return F + timedelta(seconds=config.get_srs_time(nivl_srs))
    #SETTER###################################
    def set_fecha_creacion(self,fecha_creacion):
        self.fecha_creacion = fecha_creacion
    def set_nivel_srs(self,nivel_srs):
        self.nivel_srs = nivel_srs
    def set_palabra(self,palabra):
        self.palabra = palabra
    #DB#######################################
    def add_data(self,*arg):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."FLASHCARD" (fla_id,fla_tipo,fla_nivel_srs) VALUES (%s,%s,%s) ON CONFLICT (fla_id) DO UPDATE SET fla_nivel_srs = excluded.fla_nivel_srs"""
        data = (self.id,self.tipo,self.nivel_srs)
        return psc.query(psql_query,data)
        
    def del_data(self,*arg):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."FLASHCARD" WHERE fla_id = %s;"""
        data = (self.id,)
        d = psc.query(psql_query,data)
        return self.revision_list.del_data() + d


if __name__ == "__main__":
    f = Flashcard('get-d1s7:NicoffeeFR',None,'reco',datetime.now(),RevisionList(list()))
    print("Exito al agregar fal. Filas afectadas: ",f.add_data())
    print("Exito al eliminar fal. Filas afectadas: ",f.del_data())