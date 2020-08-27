from Flashcard import Flashcard
from datetime import datetime,timedelta
from database.Database import PSConnection
from interface.DBWriter import DBWriter
class FlashcardList(DBWriter):
    def __init__(self,flashcard_list):
        self.flashcard_list = flashcard_list

    def __len__(self):
        return len(self.flashcard_list)

    def __iter__(self):
        for f in self.flashcard_list:
            yield f

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
            i = 0
            while i<len(L) and d_fcard >= L[i].get_fecha_sig():
                i+=1
            if i >= len(L):
                L.append(flashcard)
            else:
                L.insert(i,flashcard)
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
    def list_review_disponible(self,fecha = datetime.now()):
        L_disponible = FlashcardList(flashcard_list = [])
        for F in self.flashcard_list:
            if F.get_fecha_sig() < fecha:
                L_disponible.agregar_flashcard(F)
        return L_disponible
    #
    #
    #
    #
    #
    def cant_flashcard(self,nivel=None):
        if nivel is None:
            return len(self.flashcard_list)
        else:
            c = 0
            for f in self.flashcard_list:
                if f.get_nivel_srs() == nivel:
                    c += 1
            return c
    #
    #
    #
    #
    #
    def cant_rev_per_hour(self,desde=datetime.now(),horas=24):
        hour_l = [0]*horas
        desde.replace(hour=0,minute=0,second=0)
        for flsh in self.flashcard_list:
            f_date = flsh.get_fecha_sig()
            if f_date<=(desde+timedelta(hours=horas)):
                for i in range(horas):
                    if (f_date<=desde+timedelta(hours=i+1)):
                        hour_l[i] = hour_l[i] + 1
                        break
        return hour_l 

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