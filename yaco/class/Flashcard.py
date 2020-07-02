from RevisionList import RevisionList
from datetime import datetime,timedelta
from config import config
class Flashcard:
    def __init__(
            self,
            id, #{id palabra}-{fr | fp}
            palabra,
            tipo, #reco, prod
            fecha_creacion = datetime.now(),
            nivel_srs = 1,
            revision_list = RevisionList()):
        self.id = id
        self.palabra = palabra
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.nivel_srs = nivel_srs
        self.revision_list = revision_list
    #
    #
    #
    #
    #
    def completar_revision(self,es_correcta,fecha = datetime.now()):
        self.revision_list.completar_revision(self.id,fecha,self.nivel_srs,(False if es_correcta else True))
        self.nivel_srs = self.nivel_srs + (1 if es_correcta else -1)
    #
    #
    #
    #
    #

    #GETTER###################################
    def get_id(self):
        return self.id
    def get_tipo(self):
        return self.tipo
    def get_fecha_creacion(self):
        return self.fecha_creacion
    def get_nivel_srs(self):
        return self.nivel_srs
    def get_fecha_sig(self):
        rev_list = self.revision_list
        nivl_srs = self.nivel_srs
        F = self.rev_list.get_fecha_ult_rev()
        if F is None:
            return self.get_fecha_creacion + timedelta(seconds=config.get_srs_time(1))
        else:
            return F + timedelta(seconds=config.get_srs_time(nivl_srs))
    #SETTER###################################
    def set_fecha_creacion(self,fecha_creacion):
        self.fecha_creacion = fecha_creacion
    def set_nivel_srs(self,nivel_srs):
        self.nivel_srs = nivel_srs
    def set_palabra(self,palabra):
        self.palabra = palabra