from Flashcard import Flashcard
class FlashcardList:
    def __init__(self,flashcard_list = []):
        self.flashcard_list = flashcard_list
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
    #GETTER###################################
    #SETTER###################################