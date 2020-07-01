from Palabra import Palabra
from Definicion import Definicion
class PalabraDict:
    lang = ['en','es']
    def __init__(self):
        self.dict_id  = {}
        self.dict_lang = {}
        for l in PalabraDict.lang:
            self.dict_lang[l] = {}
    @classmethod
    def from_db(cls,usu_id):
        pass
    #
    #
    #
    #
    #
    def agregar_palabra(self,palabra_info):
        P = Palabra.from_dict(palabra_info)
        p_id = P.get_id_key()
        if p_id in self.dict_id:
            self.dict_id[p_id].append(P)
        else:
            self.dict_id[p_id] = [P]
        def add_in_dict(idioma,dict):
            for key in P.get_definicion_key_iter(idioma):
                if key in dict:
                    dict[key].append(P)
                else:
                    dict[key] = [P]
        for l in PalabraDict.lang:
            add_in_dict(l,self.dict_lang[l])
        return P
    #
    #
    #
    #
    #
    def eliminar_palabra(self,id):
        def pop_in_list(L,id):
            index = None
            for i in range(len(L)):
                p = L[i]
                if p.get_id() == id:
                    index = i
            return None if index is None else L.pop(i)
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
    def existe_palabra(self,palabra):
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
    def palabras_con_definicion(self,definicion,idioma):
        try:
            L = []
            key = Definicion.to_key(definicion)
            for w in self.dict_lang[idioma][key]:
                if w.contiene_definicion(definicion,idioma):
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
    @staticmethod
    def __palabra_en_celda(palabra,dict,key):
        try:
            for p in dict[key]:
                if palabra.es_igual(p):
                    return True
        except KeyError as err:
            print("Error al entrar a la celda ",err)
        return False

    #GETTER###################################
    #SETTER###################################







if __name__ == "__main__":
    from function import Desglose
    from function import GetWord
    import json
    pd = PalabraDict()
    print("Crear diccionario")
    for l in PalabraDict.lang:
        print(pd.dict_lang[l])
    ##########################
    print("Agregar una palabra")
    resp = GetWord.get_word('get')
    w_json = Desglose.desglose(resp)
    w_dic = json.loads(w_json)
    for w in w_dic:
        pd.agregar_palabra(w)
    print(pd.dict_id)
    for l in PalabraDict.lang:
        print(pd.dict_lang[l])
    print("Existe una palabra")
    #print(pd.existe_palabra(p))
    print("Eliminar una palabra")
    print("PE") if pd.eliminar_palabra("get-d1s2") is not None else print("PNE")
    print("PE") if pd.eliminar_palabra("estaPalabra-noExiste") is not None else print("PNE")