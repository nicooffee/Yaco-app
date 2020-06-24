from datetime import datetime,timedelta
from Revision import Revision
import config.config
class RevisionList:
    def __init__(self,revision_actual = Revision(),revision_list=[]):
        self.revision_list = revision_list
        self.actual_incorrecto = False

    #
    #
    #
    #
    #
    def get_fecha_rev_sig(self,srs_lvl):
        rev_L = self.revision_list
        if len(rev_L)>0
            return rev_L[0].get_fecha() + timedelta(seconds=config.get_srs_time(srs_lvl))

    def completar_revision(self,fecha,nivel_srs):
        pass
    #GETTER###################################
    #SETTER###################################