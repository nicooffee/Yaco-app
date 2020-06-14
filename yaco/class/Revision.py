import datetime
class Revision:
    def __init__(self,fecha= datetime.datetime.now(),es_correcto=False,equivocacion_previa=False):
        self.fecha = fecha
        self.es_correcto = es_correcto
        self.equivocacion_previa = equivocacion_previa

    
    ###################################
    def get_fecha(self):
        return self.fecha
    def get_es_correcto(self):
        return self.es_correcto
    def get_equivocacion_previa(self):
        return self.equivocacion_previa
    ######
    def set_fecha(self,fecha):
        self.fecha = fecha
    def set_es_correcto(self,es_correcto):
        self.es_correcto = es_correcto
    def set_equivocacion_previa(self,equivocacion_previa):
        self.equivocacion_previa = equivocacion_previa