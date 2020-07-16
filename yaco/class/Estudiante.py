from Usuario import Usuario
from FlashcardList import FlashcardList
from PalabraDict import PalabraDict
from Flashcard import Flashcard
from Palabra import Palabra
from interface.DBWriter import DBWriter
import datetime
from database.Database import PSConnection
class Estudiante(Usuario):
    def __init__(
            self,
            nombre_usuario,
            tipo_estudiante,
            flashcard_list = FlashcardList(),
            palabra_dict = PalabraDict(),
            fecha_registro = datetime.datetime.now(),
            ultimo_logeo = datetime.datetime.now(),
            exp_total = 0):
        super().__init__(nombre_usuario,flashcard_list,palabra_dict,fecha_registro,ultimo_logeo)
        self.tipo_estudiante = tipo_estudiante
        self.exp_total = exp_total

    #GETTER###################################
    def get_tipo_estudiante(self):
        return self.tipo_estudiante
    def get_exp_total(self):
        return self.exp_total
    #SETTER###################################

    def set_tipo_estudiante(self,tipo_estudiante):
        self.tipo_estudiante = tipo_estudiante
    def set_exp_total(self,exp_total):
        self.exp_total = exp_total

    #DB#######################################
    def add_data(self,*arg):
        if len(arg)>0 and isinstance(arg[0],str):
            psql_query_u = """INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro) VALUES (%s,%s,%s)"""
            psql_query_e = """INSERT INTO PUBLIC."ESTUDIANTE" (usu_id,est_tipo,est_exp_total) VALUES (%s,%s,%s);"""
            data_u = (self.id,arg[0],self.fecha_registro)
            data_e = (self.id,self.tipo_estudiante,self.exp_total)
            psc = PSConnection()
            r_u = psc.query(psql_query_u,data_u)
            r_e = psc.query(psql_query_e,data_e)
            return -1 if r_u == -1 or r_e == -1 else r_u+r_e
        return -1

if __name__ == "__main__":
    E = Estudiante("Nicoffee","free")
    print("Agregar estudiante a bdd: ",E.add_data("1234"))
    from function import Desglose
    from function import GetWord
    import json
    print("Agregar una palabra")
    resp = GetWord.get_word('to%20go%20out')
    w_json = Desglose.desglose(resp)
    w_dic = json.loads(w_json)
    for w in w_dic:
        E.agregar_palabra(w)
    #print("Eliminar estudiante de bdd: ",E.del_data())