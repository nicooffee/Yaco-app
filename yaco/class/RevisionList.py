from datetime import datetime,timedelta
from Revision import Revision
from interface.DBWriter import DBWriter
from database.Database import PSConnection
class RevisionList(DBWriter):
    def __init__(self,revision_list=[]):
        self.revision_list = revision_list
    @classmethod
    def from_db(cls,fla_id):
        psc = PSConnection()
        psql_query = """SELECT PUBLIC."REVISION".rev_id,rev_fla_fecha,rev_nivel_srs,rev_es_completa,rev_equivocacion_previa
                        FROM PUBLIC."REVISION"
                        INNER JOIN PUBLIC."FLASHCARD_REVISION" ON PUBLIC."REVISION".rev_id = PUBLIC."FLASHCARD_REVISION".rev_id
                        WHERE fla_id = %s
                        ORDER BY rev_fla_fecha DESC"""
        data = (fla_id,)
        res = psc.fetch_all(psql_query,data)
        return RevisionList(revision_list=list(map(lambda x: Revision(x[0],x[1],x[2],r[3],r[4]),res)))
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

    #DB#######################################
    def add_data(self,*arg):
        psc = PSConnection()
        psql_query = """INSERT INTO PUBLIC."REVISION" (rev_id,rev_es_completa,rev_equivocacion_previa,rev_nivel_srs) VALUES (%s,%s,%s,%s)"""
        data_list = map(lambda x: x.get_bd_info(),self.revision_list)
        return psc.query_many(psql_query,data_list)
    def del_data(self,*arg):
        psc = PSConnection()
        psql_query = """DELETE from PUBLIC."REVISION" WHERE rev_id = %s;"""
        data_list = map(lambda x: (x.get_id(),),self.revision_list)
        return psc.query_many(psql_query,data_list)

if __name__ == "__main__":
    R_l = RevisionList()
    print(R_l.get_fecha_ult_rev())
    R_l.completar_revision("fla",datetime.now(),1,False)
    print(R_l.get_fecha_ult_rev())