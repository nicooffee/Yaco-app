from Flashcard import Flashcard
from datetime import datetime
from database.Database import PSConnection
from interface.DBWriter import DBWriter
class FlashcardList(DBWriter):
    def __init__(self,flashcard_list = []):
        self.flashcard_list = flashcard_list
    @classmethod
    def from_db(cls,usu_id,pal_id):
        pass
    #
    #
    #
    #
    #
    def agregar_flashcard(self,flashcard):
        L = self.flashcard_list
        if len(L)==0:
            L.append(flashcard)
        else:
            d_fcard = flashcard.get_fecha_sig()
            for i in range(len(L)):
                d_fcard_aux = L[i].get_fecha_sig()
                if d_fcard>d_fcard_aux:
                    L.insert(i,flashcard)
                    return flashcard
                if i == len(L) - 1:
                    L.append(flashcard)
        return flashcard
    #
    #
    #
    #
    #
    def eliminar_flashcard(self,id):
        for i in range(len(self.flashcard_list)):
            f = self.flashcard_list[i]
            if f.get_id() == id:
                return self.flashcard_list.pop(i)
        return None
    #
    #
    #
    #
    #
    def fcard_review_disponible(self,fecha = datetime.now()):
        L_disponible = FlashcardList()
        for F in self.flashcard_list:
            if F.get_fecha_sig() < fecha:
                L_disponible.agregar_flashcard(F)
    #
    #
    #
    #
    #
    #GETTER###################################
    def get_cant_fcard(self):
        return len(self.flashcard_list)
    def get_id_iter(self):
        for f in self.flashcard_list:
            yield f.get_id()
    #SETTER###################################

    #DB#######################################
    def add_data(self,*arg):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."FLASHCARD" (fla_id,fla_tipo,fla_nivel_srs) VALUES (%s,%s,%s)"""
        data_list = map(lambda x: (x.get_id(),x.get_tipo(),x.get_nivel_srs()),self.flashcard_list)
        return psc.query_many(psql_query,data_list)
        
    def del_data(self,*arg):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."FLASHCARD" WHERE fla_id = %s;"""
        data = map(lambda x: (x.id,),self.flashcard_list)
        return psc.query_many(psql_query,data)

if __name__ == "__main__":
    pass