class Definicion:
    def __init__(self,definicion,info_adicional = "",es_principal = False):
        self.definicion = definicion
        self.info_adicional = info_adicional
        self.es_principal = es_principal
    #
    #
    #
    #
    #
    def es_igual(self,definicion):
        return True if self.definicion == definicion else False

    #GETTER###################################
    def get_definicion(self):
        return self.definicion
    def get_info_adicional(self):
        return self.info_adicional
    def get_es_principal(self):
        return self.es_principal

    def get_key(self):
        return self.definicion[0:2].tolower()
    #SETTER###################################
    def set_definicion(self,definicion):
        self.definicion = definicion
    def set_info_adicional(self,info_adicional):
        self.info_adicional = info_adicional
    def set_es_principal(self,es_principal):
        self.es_principal = es_principal