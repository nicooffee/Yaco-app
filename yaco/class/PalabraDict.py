from Palabra import Palabra
class PalabraDict:
    def __init__(self):
        self.dict_id  = {}
        self.dict_esp = {}
        self.dict_eng = {}
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
        add_in_dict('en',self.dict_eng)
        add_in_dict('es',self.dict_esp)
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
                for key in p.get_definicion_key_iter('es'):
                    pop_in_list(self.dict_esp[key],id)
                    if len(self.dict_esp[key]) == 0:
                        self.dict_esp.pop(key)
                for key in p.get_definicion_key_iter('en'):
                    pop_in_list(self.dict_eng[key],id)
                    if len(self.dict_eng[key]) == 0:
                        self.dict_eng.pop(key)
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
    pd = PalabraDict()
    print("Crear diccionario")
    print(pd.dict_esp)
    print(pd.dict_eng)
    ##########################
    print("Agregar una palabra")
    dic =     {
        "id": "get-d1s7",
        "tipo": "transitive verb",
        "definicion_eng": [
            ["get",""]
        ],
        "definicion_esp": [
            ["agarrar",""],["capturar",""]
        ],
        "es_ofensiva": False
    }
    p = pd.agregar_palabra(dic)
    print(pd.dict_id)
    print(pd.dict_esp)
    print(pd.dict_eng)
    print("Existe una palabra")
    print(pd.existe_palabra(p))
    print("Eliminar una palabra")
    pd.eliminar_palabra(p.get_id())
    print(pd.dict_id)
    print(pd.dict_esp)
    print(pd.dict_eng)