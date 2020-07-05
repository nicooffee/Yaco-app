import datetime
from interface.DBWriter import DBWriter
from database.Database import PSConnection
class Revision(DBWriter):
    def __init__(self,id,fecha= datetime.datetime.now(),nivel_srs=1,es_completa=False,equivocacion_previa=False):
        self.id = id #{id flashcard}{numero rev}
        self.fecha = fecha
        self.nivel_srs = nivel_srs
        self.es_completa = es_completa
        self.equivocacion_previa = equivocacion_previa
    #
    #
    #
    #
    #
    
    #GETTER###################################
    def get_id(self):
        return self.id
    def get_fecha(self):
        return self.fecha
    def get_nivel_srs(self):
        return self.nivel_srs
    def get_es_completa(self):
        return self.es_completa
    def get_equivocacion_previa(self):
        return self.equivocacion_previa
    def get_bd_info(self):
        return (self.id,self.es_completa,self.equivocacion_previa,self.nivel_srs)
    #SETTER###################################
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_es_completa(self,es_completa):
        self.es_completa = es_completa
    def set_equivocacion_previa(self,equivocacion_previa):
        self.equivocacion_previa = equivocacion_previa
    #DB#######################################
    def add_data(self):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."REVISION" (rev_id,rev_es_completa,rev_equivocacion_previa,rev_nivel_srs) VALUES (%s,%s,%s,%s)"""
        data = (self.id,self.es_completa,self.equivocacion_previa,self.nivel_srs)
        return psc.query(psql_query,data)
    def del_data(self):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."REVISION" WHERE rev_id = %s;"""
        data = (self.id,)
        return psc.query(psql_query,data)

if __name__ == "__main__":
    r = Revision('get-d1s5:NicoffeeFR0')
    print("Exito al agregar def. Filas afectadas: ",r.add_data())
    print("Exito al eliminar def. Filas afectadas: ",r.del_data())