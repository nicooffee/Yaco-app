from FlashcardList import FlashcardList
from PalabraDict import PalabraDict
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