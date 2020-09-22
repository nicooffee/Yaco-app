from Palabra import Palabra
from Definicion import Definicion
from DefinicionList import DefinicionList
from RevisionList import RevisionList
from FlashcardList import FlashcardList
from database.Database import PSConnection
from Flashcard import Flashcard
class PalabraDict:
    lang = ['en','es']
    def __init__(self):
        self.dict_id  = {}
        self.dict_lang = {}
        for l in PalabraDict.lang:
            self.dict_lang[l] = {}
    @classmethod
    def from_db(cls,connection,usu_id):
        psc = connection
        psql_query = """SELECT PUBLIC."PALABRA".pal_id,pal_tipo,pal_es_ofensiva,PUBLIC."FLASHCARD".fla_id,fla_fecha_creacion,fla_nivel_srs,fla_tipo
                        FROM PUBLIC."PALABRA"
                        INNER JOIN PUBLIC."USU_PAL_FLASHCARD" ON PUBLIC."PALABRA".pal_id = PUBLIC."USU_PAL_FLASHCARD".pal_id
                        INNER JOIN PUBLIC."FLASHCARD" ON PUBLIC."USU_PAL_FLASHCARD".fla_id = PUBLIC."FLASHCARD".fla_id
                        WHERE PUBLIC."USU_PAL_FLASHCARD".usu_id = %s
                        ORDER BY PUBLIC."PALABRA".pal_id ASC;"""
        data = (usu_id,)
        res = psc.fetch_all(psql_query,data)
        dic = cls()
        p_aux = None
        for r in res:
            if p_aux is None or p_aux.get_id() != r[0]:
                if p_aux is not None:
                    dic.__add_in_dict(p_aux)
                    p_aux = None
                p_aux = Palabra(r[0],r[1],r[2],
                                definicion_eng=DefinicionList.from_db(psc,usu_id,r[0],Palabra.lang[0]),
                                definicion_esp=DefinicionList.from_db(psc,usu_id,r[0],Palabra.lang[1]))
                f = Flashcard(r[3],p_aux,r[6],fecha_creacion=r[4],revision_list=RevisionList.from_db(connection,r[3]),nivel_srs=r[5])
                p_aux.set_flashcard(f)
            else:
                f = Flashcard(r[3],p_aux,r[6],fecha_creacion=r[4],revision_list=RevisionList.from_db(connection,r[3]),nivel_srs=r[5])
                p_aux.set_flashcard(f)
                dic.__add_in_dict(p_aux)
                p_aux = None
        return dic
    #
    #
    #
    #
    #
    def __add_in_dict(self,palabra):
        if palabra is not None:
            def add_in_dict(idioma,dict):
                for key in palabra.get_definicion_key_iter(idioma):
                    if key in dict:
                        dict[key].append(palabra)
                    else:
                        dict[key] = [palabra]
            p_id = palabra.get_id_key()
            if p_id in self.dict_id:
                self.dict_id[p_id].append(palabra)
            else:
                self.dict_id[p_id] = [palabra]
            for l in PalabraDict.lang:
                add_in_dict(l,self.dict_lang[l])
        return palabra
    #
    #
    #
    #
    #
    def agregar_palabra(self,palabra_info: dict,uq_id: str):
        P = Palabra.from_dict(palabra_info,uq_id)
        self.__add_in_dict(P)
        return P
    #
    #
    #
    #
    #
    def eliminar_palabra(self,id: str):
        def pop_in_list(L,id):
            index = None
            for i in range(len(L)):
                if L[i].get_id() == id:
                    return L.pop(i)
            return None 
        if Palabra.es_id_valido(id):
            try:
                p = pop_in_list(self.dict_id[Palabra.to_key(id)],id)
                if len(self.dict_id[Palabra.to_key(id)]) == 0:
                    self.dict_id.pop(Palabra.to_key(id))
                for l in PalabraDict.lang:
                    for key in p.get_definicion_key_iter(l):
                        pop_in_list(self.dict_lang[l][key],id)
                        if len(self.dict_lang[l][key]) == 0:
                            self.dict_lang[l].pop(key)
                return p
            except KeyError:
                return None
        return None
    #
    #
    #
    #
    #
    def existe_palabra(self,palabra: Palabra):
        key = palabra.get_id_key()
        if key in self.dict_id:
            for w in self.dict_id[key]:
                if self.__palabra_en_celda(palabra,self.dict_id,key):
                    return True
        return False
    #
    #
    #
    #
    #
    def palabras_con_def_str(self,def_str: str,idioma: str):
        try:
            L = []
            key = Definicion.to_key(def_str)
            for w in self.dict_lang[idioma][key]:
                if w.contiene_def_str(def_str,idioma):
                    L.append(w)
            return L
        except KeyError as err:
            print("Error al entrar a la celda ",err)
            return []
    #
    #
    #
    #
    #
    def palabras_cruz_paldef(self,palabra: Palabra,def_str: str,idioma: str):
        pal_list = self.palabras_con_def_str(def_str,idioma)
        L = []
        for w in pal_list:
            if palabra.contiene_def_comun.contiene_def_comun(w,Palabra.idioma_contrario(idioma)):
                L.append(w)
        return L
    #
    #
    #
    #
    #
    def cant_palabra(self):
        s = 0
        for value in self.dict_id.values():
            s = s + len(value)
        return s
    #
    #
    #
    #
    #
    @staticmethod
    def __palabra_en_celda(palabra,dict: dict,key: str):
        try:
            for p in dict[key]:
                if palabra == p:
                    return True
        except KeyError as err:
            print("Error al entrar a la celda ",err)
        return False

    #GETTER###################################
    def get_flashcard_list(self):
        flist = FlashcardList(list())
        for key,value in self.dict_id.items():
            for w in value:
                for f in w.get_flashcard_list():
                    flist.agregar_flashcard(f)
        return flist

    def get_palabra_iter(self):
        for key,value in self.dict_id.items():
            for w in value:
                yield w

    def get_palabra(self,id):
        try:
            key = Palabra.to_key(id)
            for p in self.dict_id[key]:
                if p.get_id() == id:
                    return p
            return None
        except KeyError:
            return None
    #SETTER###################################







if __name__ == "__main__":
    from function import Desglose
    from function import GetWord
    import json
    #pd = PalabraDict()
    print("Crear diccionario")
    for l in PalabraDict.lang:
        print(pd.dict_lang[l])
    ##########################
    print("Agregar una palabra")
    resp = GetWord.get_word('to%20go%20out')
    w_json = Desglose.desglose(resp)
    w_dic = json.loads(w_json)
    for w in w_dic:
        pd.agregar_palabra(w,'Nicoffee')
    print(pd.dict_id)
    for l in PalabraDict.lang:
        print(pd.dict_lang[l])
    print("Existe una palabra")
    #print(pd.existe_palabra(p))
    print("Eliminar una palabra")
    #print("PE") if pd.eliminar_palabra("get-d1s2") is not None else print("PNE")
    print("PE") if pd.eliminar_palabra("estaPalabra-noExiste") is not None else print("PNE")
    for key in pd.dict_id.keys():
        for w in pd.dict_id[key]:
            w.add_data()
    pd = PalabraDict.from_db('Nicoffee')