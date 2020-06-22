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
            F = Flashcard(P)
            P.set_flashcard(F)
            self.flashcard_list.agregar_flashcard(F)
            

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