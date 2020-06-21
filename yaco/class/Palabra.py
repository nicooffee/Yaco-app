from DefinicionList import DefinicionList
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
        return cls(
            id=palabra_info["id"],
            tipo=palabra_info["tipo"],
            definicion_eng=DefinicionList.from_string_list(palabra_info["definicion_eng"]),
            definicion_esp=DefinicionList.from_string_list(palabra_info["definicion_esp"]),
            es_ofensiva=palabra_info["es_ofensiva"])

    #GETTER###################################
    def get_id(self):
        return self.id
    def get_tipo(self):
        return self.tipo
    def get_es_ofensiva(self):
        return self.es_ofensiva
    #SETTER###################################
    def set_id(self,id):
        self.id = id
    def set_tipo(self,tipo):
        self.tipo = tipo
    def set_es_ofensiva(self,es_ofensiva):
        self.es_ofensiva = es_ofensiva


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
    Palabra.from_dict(dic)