from Definicion import Definicion
class DefinicionList:
    def __init__(self,definicion_list = []):
        self.definicion_list = definicion_list

    @classmethod
    def from_def_list(cls,definicion_list):
        L = []
        for d in definicion_list:
            L.append(d)
        return cls(definicion_list=L)

    @classmethod
    def from_string_list(cls,string_list):
        L = []
        for i in range(len(string_list)):
            s = string_list[i]
            d = Definicion(s[0],s[1],True if i==0 else False)
            L.append(d)
        return cls(definicion_list=L)


    #GETTER###################################
    def get_iter(self):
        for x in self.definicion_list:
            yield x

    def get_key_iter(self):
        for x in self.definicion_list:
            yield x.get_key()
    #SETTER###################################


if __name__ == "__main__":

    dic =     {
        "id": "get-d1s7",
        "tipo": "transitive verb",
        "definicion_eng": [
            [
                "get",
                ""
            ]
        ],
        "definicion_esp": [
            [
                "agarrar",
                ""
            ],
            [
                "capturar",
                ""
            ]
        ],
        "es_ofensiva": False
    }
    DefinicionList.from_string_list(dic["definicion_esp"])
    DefinicionList.from_string_list(dic["definicion_eng"])