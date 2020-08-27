import datetime
from interface.DBWriter import DBWriter
from database.Database import PSConnection
class Revision(DBWriter):
    def __init__(self,id,fecha= datetime.datetime.now(),nivel_srs=1,es_correcta=False):
        self.id = id 
        self.fecha = fecha
        self.nivel_srs = nivel_srs
        self.es_correcta = es_correcta
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
    def get_es_correcta(self):
        return self.es_correcta
    def get_bd_info(self):
        return (self.id,self.es_correcta,self.nivel_srs)
    #SETTER###################################
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_es_correcta(self,es_correcta):
        self.es_correcta = es_correcta
    #DB#######################################
    def add_data(self,*arg):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."REVISION" (rev_id,rev_es_correcta,rev_nivel_srs) VALUES (%s,%s,%s)"""
        data = (self.id,self.es_correcta,self.nivel_srs)
        return psc.query(psql_query,data)
    def del_data(self,*arg):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."REVISION" WHERE rev_id = %s;"""
        data = (self.id,)
        return psc.query(psql_query,data)

if __name__ == "__main__":
    r = Revision('get-d1s5:NicoffeeFR0')
    print("Exito al agregar rev. Filas afectadas: ",r.add_data())
    print("Exito al eliminar rev. Filas afectadas: ",r.del_data())