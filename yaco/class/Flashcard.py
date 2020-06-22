from Palabra import Palabra
from RevisionList import RevisionList
import datetime
class Flashcard:
    def __init__(
            self,
            palabra,
            fecha_creacion = datetime.datetime.now(),
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

    #GETTER###################################
    def get_fecha_creacion(self):
        return self.fecha_creacion
    def get_nivel_srs_reco(self):
        return self.nivel_srs_reco
    def get_nivel_srs_prod(self):
        return self.nivel_srs_prod
    def get_min_fecha_rev(self):
        d_reco = self.revision_list_reco.get_fecha_rev_sig()
        d_prod = self.revision_list_prod.get_fecha_rev_sig()
        return d_reco if d_reco<d_prod else d_prod
    #SETTER###################################
    def set_fecha_creacion(self,fecha_creacion):
        self.fecha_creacion = fecha_creacion
    def set_nivel_srs_reco(self,nivel_srs_reco):
        self.nivel_srs_reco = nivel_srs_reco
    def set_nivel_srs_prod(self,nivel_srs_prod):
        self.nivel_srs_prod = nivel_srs_prod