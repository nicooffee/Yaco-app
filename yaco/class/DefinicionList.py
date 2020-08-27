from Definicion import Definicion
from database.Database import PSConnection
from interface.DBWriter import DBWriter
class DefinicionList(DBWriter):
    def __init__(self,definicion_list):
        self.definicion_list = definicion_list

    def __add__(self,other):
        return DefinicionList(definicion_list=self.definicion_list + other.definicion_list)

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
            d = Definicion(pal_id+':'+idioma+"{:02}".format(i),s[0],idioma,s[1],True if i==0 else False,False)
            L.append(d)
        return cls(definicion_list=L)
    
    @classmethod
    def from_db(cls,usu_id,pal_id,idioma = None):
        psc = PSConnection()
        psql_query = """SELECT PUBLIC."DEFINICION".def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra
                        FROM PUBLIC."DEFINICION"
                        INNER JOIN PUBLIC."USU_PAL_DEFINICION" ON PUBLIC."DEFINICION".def_id = PUBLIC."USU_PAL_DEFINICION".def_id
                        WHERE usu_id = %s AND pal_id = %s"""
        if idioma is not None:
            psql_query = """SELECT PUBLIC."DEFINICION".def_id,def_definicion,def_idioma,def_info_adicional,def_principal,def_extra
                            FROM PUBLIC."DEFINICION"
                            INNER JOIN PUBLIC."USU_PAL_DEFINICION" ON PUBLIC."DEFINICION".def_id = PUBLIC."USU_PAL_DEFINICION".def_id
                            WHERE usu_id = %s AND pal_id = %s AND def_idioma = %s;"""
        data = (usu_id,pal_id) if idioma is None else (usu_id,pal_id,idioma)
        res = psc.fetch_all(psql_query,data)
        return cls(definicion_list=list(map(lambda x: Definicion(x[0],x[1],x[2],x[3],x[4],x[5]),res)))
    #
    #
    #
    #
    #
    def agregar_definicion(self,id,definicion,info_adicional,idioma):
        d = Definicion(id,definicion,idioma,info_adicional=info_adicioanl,es_principal=False,es_extra=True)
        self.definicion_list.append(d)
        return d
    #
    #
    #
    #
    #
    def eliminar_definicion(self,def_id):
        for i in len(self.definicion_list):
            if self.definicion_list[i].get_id() == def_id:
                return self.definicion_list.pop(i)
        return None
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
    def get_new_id_index(self):
        id_index = []
        for d in self.definicion_list:
            if d.get_es_extra():
                id_index.append(int(d.get_id()[-2:]))
        if len(id_index) == 0:
            return '00'
        elif len(id_index)>=100:
            raise IndexError("Excede la cantidad máxima de definiciones")
        else:
            for n_id in range(100):
                if n_id not in id_index:
                    return n_id

    def get_definicion_principal(self):
        for d in self.definicion_list:
            if d.get_es_principal():
                return d
        return self.definicion_list[0]

    def get_def_extra(self):
        L = filter(lambda d: d.get_es_extra(),self.definicion_list)
        return DefinicionList(definicion_list=list(L))
    #SETTER###################################
    def add_data(self,*arg):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."DEFINICION" (def_id,def_definicion,def_idioma,def_info_adicional) 
                        VALUES (%s,%s,%s,%s)
                        ON CONFLICT (def_id) DO UPDATE
                        SET def_definicion = excluded.def_definicion,
                            def_idioma = excluded.def_idioma,
                            def_info_adicional = excluded.def_info_adicional;"""
        data_list = map(lambda x: x.get_bd_info(),self.definicion_list)
        return psc.query_many(psql_query,data_list)
    def del_data(self,*arg):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."DEFINICION" WHERE def_id = %s;"""
        data_list = map(lambda x: (x.get_id(),),self.definicion_list)
        return psc.query_many(psql_query,data_list)
if __name__ == "__main__":
    dl = DefinicionList.from_db('Nicoffee','go:1-d1s18','en')
