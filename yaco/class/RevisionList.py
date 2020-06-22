from datetime import datetime,timedelta
from Revision import Revision
class RevisionList:
    def __init__(self,revision_actual = Revision(),revision_list=[]):
        self.revision_actual = revision_actual
        self.revision_list = revision_list
    
    @classmethod
    def from_date(cls,fecha):
        #CAMBIAR ESTO POR ARCHIV CONFIG
        R = Revision(fecha=fecha+timedelta(hours=3))
        return cls(revision_actual=R)
    #
    #
    #
    #
    #
    def get_fecha_rev_sig(self):
        return self.revision_actual.get_fecha()
    #GETTER###################################
    #SETTER###################################