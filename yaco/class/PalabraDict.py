import string
from Palabra import Palabra
class PalabraDict:
    def __init__(self):
        self.dict_esp = {}
        self.dict_eng = {}
        letters = string.ascii_lowercase
        for x in letters:
            for y in letters:
                self.dict_esp[x+y] = []
                self.dict_eng[x+y] = []
    #
    #
    #
    #
    #
    def agregar_palabra(palabra_info):
        pass
    #
    #
    #
    #
    #
    #GETTER###################################
    #SETTER###################################







if __name__ == "__main__":
    pd = PalabraDict()
    print("Crear diccionario")
    print(pd.dict_esp)
    print(pd.dict_eng)