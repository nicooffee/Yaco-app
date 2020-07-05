from interface.DBWriter import DBWriter
from database.Database import PSConnection
class Definicion(DBWriter):
    def __init__(self,id,definicion,idioma,info_adicional = "",es_principal = False,es_extra = False):
        self.id = id #{id palabra}{idioma}{numero def}
        self.definicion = definicion
        self.idioma = idioma
        self.info_adicional = info_adicional
        self.es_principal = es_principal
        self.es_extra = es_extra

    def __eq__(self,other):
        return self.definicion == other.definicion
    #
    #
    #
    #
    #
    def is_equal(self,definicion):
        return True if self.definicion == definicion else False
    @staticmethod
    def to_key(d):
        return d[0:2].lower()
    #GETTER###################################
    def get_id(self):
        return self.id
    def get_definicion(self):
        return self.definicion
    def get_info_adicional(self):
        return self.info_adicional
    def get_es_principal(self):
        return self.es_principal
    def get_es_extra(self):
        return self.es_extra
    def get_key(self):
        return Definicion.to_key(self.definicion)
    def get_bd_info(self):
        return (self.id,self.definicion,self.idioma,self.info_adicional,self.es_principal,self.es_extra)
    #SETTER###################################
    def set_definicion(self,definicion):
        self.definicion = definicion
    def set_info_adicional(self,info_adicional):
        self.info_adicional = info_adicional
    def set_es_principal(self,es_principal):
        self.es_principal = es_principal

    #DB#######################################
    def add_data(self):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra) VALUES (%s,%s,%s,%s,%s,%s)"""
        data = (self.id,self.definicion,self.idioma,self.info_adicional,self.es_principal,self.es_extra)
        return psc.query(psql_query,data)

    def del_data(self):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."DEFINICION" WHERE def_id = %s;"""
        data = (self.id,)
        return psc.query(psql_query,data)


if __name__ == "__main__":
    d = Definicion('get-d1s5:Nicoffee1','tomar','es','(un tren, etc.)')
    print("Exito al agregar def. Filas afectadas: ",d.add_data())
    print("Exito al eliminar def. Filas afectadas: ",d.del_data())