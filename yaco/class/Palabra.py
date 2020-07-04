from DefinicionList import DefinicionList
from Flashcard import Flashcard
from interface.DBWriter import DBWriter
class Palabra(DBWriter):
    lang = ('en','es')
    def __init__(self,id,tipo,es_ofensiva,flashcard = None,definicion_eng = DefinicionList(),definicion_esp = DefinicionList()):
        self.id = id #{palabra}-s{n}d{n}:{uq_id}
        self.tipo = tipo
        self.es_ofensiva = es_ofensiva
        self.flashcard = flashcard
        self.def_lang = {Palabra.lang[0]: definicion_eng,Palabra.lang[1]: definicion_esp}
    
    @classmethod
    def from_dict(cls,palabra_info,uq_id):
        try:
            p = cls(
                id=palabra_info["id"]+':'+uq_id,
                tipo=palabra_info["tipo"],
                flashcard = [],
                definicion_eng=DefinicionList.from_string_list(palabra_info["id"],palabra_info["definicion_eng"]),
                definicion_esp=DefinicionList.from_string_list(palabra_info["id"],palabra_info["definicion_esp"]),
                es_ofensiva=palabra_info["es_ofensiva"])
            p.flashcard.append(Flashcard(p.id + "FR" ,p,'reco'))
            p.flashcard.append(Flashcard(p.id + "FP" ,p,'prod'))
            return p
        except KeyError  as err:
            print('Error de key al crear palabra',err)
            return None
    #
    #
    #
    #
    #
    def es_igual(self,palabra):
        return True if self.get_id() == palabra.get_id() else False
    #
    #
    #
    #
    #
    def contiene_def_comun(self,palabra,idioma):
        try:
            return self.def_lang[idioma].contiene_def_list(palabra.def_lang[idioma])
        except KeyError as err:
            print("Error: idioma no encontrado",err)
            return False
    #
    #
    #
    #
    #
    def contiene_def_str(self,definicion,idioma):
        try:
            return self.def_lang[idioma].contiene_def_str(definicion)
        except KeyError as err:
            print("Error: idioma no encontrado",err)
            return False
    #
    #
    #
    #
    #
    def agregar_definicion(self,definicion,info_adicional,idioma):
        try:
            return self.def_lang[idioma].agregar_definicion(definicion,info_adicional,idioma)
        except KeyError as err:
            print("Error: idioma no encontrado",err)
            return None
    #
    #
    #
    #
    #
    @staticmethod
    def es_id_valido(id):
        return True if '-' in id else False
    @staticmethod
    def to_key(id):
        return id.split('-')[0] if Palabra.es_id_valido(id) else None
    @staticmethod
    def idioma_contrario(idioma):
        if idioma == Palabra.lang[0]:
            return Palabra.lang[1]
        elif idioma == Palabra.lang[1]:
            return Palabra.lang[0]
        else:
            raise Exception("Idioma no encontrado")
    #GETTER###################################
    def get_id(self):
        return self.id

    def get_tipo(self):
        return self.tipo

    def get_es_ofensiva(self):
        return self.es_ofensiva
        
    def get_flashcard(self):
        return self.flashcard

    def get_id_key(self):
        return Palabra.to_key(self.id)

    def get_definicion_iter(self,idioma):
        try:
            return self.def_lang[idioma].get_iter()
        except KeyError as err:
            print("Error: idioma no encontrado",err)
            return empty_iter()

    def get_definicion_key_iter(self,idioma):
        try:
            return self.def_lang[idioma].get_key_iter()
        except KeyError as err:
            print("Error: idioma no encontrado",err)
            return empty_iter()
    #SETTER###################################
    def set_id(self,id):
        self.id = id
    def set_tipo(self,tipo):
        self.tipo = tipo
    def set_es_ofensiva(self,es_ofensiva):
        self.es_ofensiva = es_ofensiva
    #########################################
    def empty_iter():
        return
        yield
    #DB#######################################
    def add_data(self):
        pass
    def del_data(self):
        pass

if __name__ == "__main__":
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
    p = Palabra.from_dict(dic)
    print(p.contiene_def_str('get','en'))
    print(p.contiene_def_str('capturar','es'))
    #print(p.contiene_definicion('get','ru'))