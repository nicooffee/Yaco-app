from Flashcard import Flashcard
from datetime import datetime
class FlashcardList:
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
            d_fcard = flashcard.get_min_fecha_rev()
            for i in range(len(L)):
                d_fcard_aux = L[i].get_min_fecha_rev()
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
            if F.get_min_fecha_rev() < fecha:
                L_disponible.agregar_flashcard(F)
    #
    #
    #
    #
    #
    #GETTER###################################
    def get_cant_fcard(self):
        return len(self.flashcard_list)
    #SETTER###################################

if __name__ == "__main__":
    pass