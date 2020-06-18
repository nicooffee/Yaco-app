from DefinicionList import DefinicionList
class Palabra:
    def __init__(self,id,tipo,es_ofensiva,flashcard,definicion_eng = DefinicionList(),definicion_esp = DefinicionList()):
        self.id = id
        self.tipo = tipo
        self.es_ofensiva = es_ofensiva
        self.flashcard = flashcard
        self.definicion_eng = definicion_eng
        self.definicion_esp = definicion_esp

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