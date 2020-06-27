from DefinicionList import DefinicionList
from Flashcard import Flashcard
class Palabra:
    def __init__(self,id,tipo,es_ofensiva,flashcard = None,definicion_eng = DefinicionList(),definicion_esp = DefinicionList()):
        self.id = id
        self.tipo = tipo
        self.es_ofensiva = es_ofensiva
        self.flashcard = flashcard
        self.definicion_eng = definicion_eng
        self.definicion_esp = definicion_esp
    @classmethod
    def from_dict(cls,palabra_info):
        try:
            p = cls(
                id=palabra_info["id"],
                tipo=palabra_info["tipo"],
                flashcard = None,
                definicion_eng=DefinicionList.from_string_list(palabra_info["definicion_eng"]),
                definicion_esp=DefinicionList.from_string_list(palabra_info["definicion_esp"]),
                es_ofensiva=palabra_info["es_ofensiva"])
            p.flashcard = Flashcard(palabra_info["id"]+'f',p)
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
    def contiene_definicion(self,definicion,idioma):
        if idioma == 'en':
            return self.definicion_eng.contiene_definicion(definicion)
        elif idioma == 'es':
            return self.definicion_esp.contiene_definicion(definicion)
        else:
            raise Exception("No se encuentra el idioma entregado.")
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
        if idioma == 'en':
            return self.definicion_eng.get_iter()
        elif idioma =='es':
            return self.definicion_esp.get_iter()
        else:
            return empty_iter()

    def get_definicion_key_iter(self,idioma):
        if idioma == 'en':
            return self.definicion_eng.get_key_iter()
        elif idioma =='es':
            return self.definicion_esp.get_key_iter()
        else:
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
    print(p.contiene_definicion('get','en'))
    print(p.contiene_definicion('capturar','es'))
    #print(p.contiene_definicion('get','ru'))