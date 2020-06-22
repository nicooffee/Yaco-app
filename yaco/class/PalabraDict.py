from Palabra import Palabra
class PalabraDict:
    def __init__(self):
        self.dict_esp = {}
        self.dict_eng = {}
    #
    #
    #
    #
    #
    def agregar_palabra(self,palabra_info):
        P = Palabra.from_dict(palabra_info)
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
    pd.agregar_palabra(dic)
    print(pd.dict_esp)
    print(pd.dict_eng)