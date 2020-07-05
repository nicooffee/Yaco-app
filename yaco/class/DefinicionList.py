from Definicion import Definicion
from database.Database import PSConnection
from interface.DBWriter import DBWriter
class DefinicionList(DBWriter):
    def __init__(self,definicion_list = []):
        self.definicion_list = definicion_list

    @classmethod
    def from_def_list(cls,definicion_list):
        L = []
        for d in definicion_list:
            L.append(d)
        return cls(definicion_list=L)

    @classmethod
    def from_string_list(cls,pal_id,idioma,string_list):
        L = []
        for i in range(len(string_list)):
            s = string_list[i]
            d = Definicion(pal_id+str(i),s[0],idioma,s[1],True if i==0 else False,False)
            L.append(d)
        return cls(definicion_list=L)
    
    @classmethod
    def from_db(cls,usu_id,pal_id):
        pass
    #
    #
    #
    #
    #
    def agregar_definicion(self,definicion,info_adicional,idioma):
        d = Definicion(definicion,idioma,info_adicional=info_adicioanl,es_principal=False,es_extra=True)
        self.definicion_list.append(d)
        return d
    #
    #
    #
    #
    #
    def contiene_def(self,definicion):
        for d in self.definicion_list:
            if d == definicion:
                return True
        return False
    #
    #
    #
    #
    #
    def contiene_def_list(self,def_list):
        for d_l in def_list.get_iter():
            if self.contiene_def(d_l):
                return True
        return False
    #
    #
    #
    #
    #
    def contiene_def_str(self,definicion):
        for d in self.definicion_list:
            if d.is_equal(definicion):
                return True
        return False
    #
    #
    #
    #
    #

    #GETTER###################################
    def get_iter(self):
        for x in self.definicion_list:
            yield x
    def get_def_iter(self):
        for x in self.definicion_list:
            yield x.get_definicion()
    def get_key_iter(self):
        for x in self.definicion_list:
            yield x.get_key()
    def get_id_iter(self):
        for x in self.definicion_list:
            yield x.get_id()
    #SETTER###################################
    def add_data(self):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra) VALUES (%s,%s,%s,%s,%s,%s)"""
        data_list = map(lambda x: x.get_bd_info(),self.definicion_list)
        return psc.query_many(psql_query,data_list)
    def del_data(self):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."DEFINICION" WHERE def_id = %s;"""
        data_list = map(lambda x: (x.get_id(),),self.definicion_list)
        return psc.query_many(psql_query,data_list)
if __name__ == "__main__":

    dic =     {
        "id": "get-d1s7",
        "tipo": "transitive verb",
        "definicion_eng": [
            [
                "get",
                ""
            ]
        ],
        "definicion_esp": [
            [
                "agarrar",
                ""
            ],
            [
                "capturar",
                ""
            ]
        ],
        "es_ofensiva": False
    }
    des = DefinicionList.from_string_list(dic["definicion_esp"])
    den = DefinicionList.from_string_list(dic["definicion_eng"])
    for key in des.get_key_iter():
        print(key)
