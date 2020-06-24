import datetime
class Revision:
    def __init__(self,fecha= datetime.datetime.now(),nivel_srs=1,es_completa=False,equivocacion_previa=False):
        self.fecha = fecha
        self.nivel_srs = nivel_srs
        self.es_completa = es_completa
        self.equivocacion_previa = equivocacion_previa
    #
    #
    #
    #
    #
    def fallar(self):
        self.equivocacion_previa = True
    #
    #
    #
    #
    #
    
    #GETTER###################################
    def get_fecha(self):
        return self.fecha
    def get_nivel_srs(self):
        return self.nivel_srs
    def get_es_completa(self):
        return self.es_completa
    def get_equivocacion_previa(self):
        return self.equivocacion_previa
    #SETTER###################################
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_es_completa(self,es_completa):
        self.es_completa = es_completa
    def set_equivocacion_previa(self,equivocacion_previa):
        self.equivocacion_previa = equivocacion_previa


if __name__ == "__main__":
    Revision()