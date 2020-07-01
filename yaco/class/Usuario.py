from FlashcardList import FlashcardList
from PalabraDict import PalabraDict
from Flashcard import Flashcard
import datetime
class Usuario:
    def __init__(
            self,
            nombre_usuario,
            flashcard_list = FlashcardList(),
            palabra_dict = PalabraDict(),
            fecha_registro = datetime.datetime.now(),
            ultimo_logeo = datetime.datetime.now()):
        self.nombre_usuario = nombre_usuario
        self.flashcard_list = flashcard_list
        self.palabra_dict   = palabra_dict 
        self.fecha_registro = fecha_registro
        self.ultimo_logeo   = ultimo_logeo
    
    @classmethod
    def from_db(cls,usu_id):
        pass
    #
    #
    #
    #
    #
    #input: elemento de un desglose
    #output: palabra agregada
    def agregar_palabra(self,palabra_info):
        P = self.palabra_dict.agregar_palabra(palabra_info)
        if P is not None:
            self.flashcard_list.agregar_flashcard(P.get_flashcard())
        return P
    #
    #
    #
    #
    #
    #input: id de una palabra (de los del desglose)
    #output: palabra eliminada
    def eliminar_palabra(self,id):
        P = self.palabra_dict.eliminar_palabra(id)
        if P is not None:
            self.flashcard_list.eliminar_flashcard(P.get_flashcard().get_id())
        return P
            

    #GETTER###################################
    def get_nombre_usuario(self):
        return self.nombre_usuario
    def get_fecha_registro(self):
        return fecha_registro
    def get_ultimo_logeo(self):
        return ultimo_logeo
    #SETTER###################################
    def set_nombre_usuario(self,nombre_usuario):
        self.nombre_usuario = nombre_usuario
    def set_fecha_registro(self,fecha_registro):
        self.fecha_registro = fecha_registro
    def set_ultimo_logeo(self,ultimo_logeo):
        self.ultimo_logeo = ultimo_logeo
    
    #DB#######################################
    def db_add(self):
        pass

    def db_del(self,usu_id,pal_id):
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
    U = Usuario("nico")
    U.agregar_palabra(dic)
    print(U.palabra_dict.dict_eng)
    print(U.palabra_dict.dict_esp)
    print(U.flashcard_list.flashcard_list)
    U.eliminar_palabra(dic['id'])
    print(U.palabra_dict.dict_eng)
    print(U.palabra_dict.dict_esp)
    print(U.flashcard_list.flashcard_list)
