from Palabra import Palabra
from RevisionList import RevisionList
from datetime import datetime,timedelta
import config.config
class Flashcard:
    def __init__(
            self,
            palabra,
            fecha_creacion = datetime.now(),
            nivel_srs_reco = 1,
            nivel_srs_prod = 1,
            revision_list_reco = RevisionList(),
            revision_list_prod = RevisionList()):
        self.palabra = palabra
        self.fecha_creacion = fecha_creacion
        self.nivel_srs_reco = nivel_srs_reco
        self.nivel_srs_prod = nivel_srs_prod
        self.revision_list_reco = revision_list_reco
        self.revision_list_prod = revision_list_prod
    #
    #
    #
    #
    #
    def completar_revision_reco(self,es_correcta,fecha = datetime.now()):
        if es_correcta:
            self.revision_list_reco.completar_revision(fecha=fecha,self.nivel_srs,False)
            self.nivel_srs_reco = self.nivel_srs_reco + 1
        else:
            self.revision_list_reco.completar_revision(fecha=fecha,self.nivel_srs,True)
            self.nivel_srs_reco = self.nivel_srs_reco - 1
    #
    #
    #
    #
    #
    def completar_revision_prod(self,es_correcta,fecha = datetime.now()):
        if es_correcta:
            self.revision_list_prod.completar_revision(fecha=fecha,self.nivel_srs,False)
            self.nivel_srs_prod = self.nivel_srs_prod + 1
        else:
            self.revision_list_prod.completar_revision(fecha=fecha,self.nivel_srs,True)
            self.nivel_srs_prod = self.nivel_srs_prod - 1
    #
    #
    #
    #
    #
    def __fecha_sig(self,tipo):
        rev_list = self.revision_list_reco if tipo == 'reco' else self.revision_list_prod
        nivl_srs = self.nivel_srs_reco if tipo == 'reco' else self.nivel_srs_prod
        F = self.rev_list.get_fecha_ult_rev()
        if F is None:
            return self.get_fecha_creacion + timedelta(seconds=config.get_srs_time(1))
        else:
            return F + timedelta(seconds=config.get_srs_time(nivl_srs))#

    #GETTER###################################
    def get_fecha_creacion(self):
        return self.fecha_creacion
    def get_nivel_srs_reco(self):
        return self.nivel_srs_reco
    def get_nivel_srs_prod(self):
        return self.nivel_srs_prod
    def get_min_fecha_rev(self):
        f_reco = self.__fecha_sig('reco')
        f_prod = self.__fecha_sig('prod')
        return f_reco if f_reco<f_prod else f_prod
    #SETTER###################################
    def set_fecha_creacion(self,fecha_creacion):
        self.fecha_creacion = fecha_creacion
    def set_nivel_srs_reco(self,nivel_srs_reco):
        self.nivel_srs_reco = nivel_srs_reco
    def set_nivel_srs_prod(self,nivel_srs_prod):
        self.nivel_srs_prod = nivel_srs_prod