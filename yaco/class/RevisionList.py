from datetime import datetime,timedelta
from Revision import Revision
class RevisionList:
    def __init__(self,revision_list=[]):
        self.revision_list = revision_list
        self.actual_incorrecto = False
    @classmethod
    def from_db(cls,usu_id,pal_id):
        pass
    #
    #
    #
    #
    #
    def completar_revision(self,fla_id,fecha,nivel_srs,eq_previa):
        R = Revision(id=fla_id+str(len(self.revision_list)),fecha=fecha,nivel_srs=nivel_srs,es_completa=True,equivocacion_previa=eq_previa)
        self.revision_list.insert(0,R)
        return R
    #GETTER###################################
    def get_fecha_ult_rev(self):
        rev_L = self.revision_list
        if len(rev_L)>0:
            return rev_L[0].get_fecha()
        else:
            return None
    #SETTER###################################

if __name__ == "__main__":
    R_l = RevisionList()
    print(R_l.get_fecha_ult_rev())
    R_l.completar_revision("fla",datetime.now(),1,False)
    print(R_l.get_fecha_ult_rev())