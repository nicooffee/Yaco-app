import psycopg2
import DatabaseData as dbdata
class PSConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            user=dbdata.user,
            password=dbdata.db_model_pswd,
            host=dbdata.host,
            port=dbdata.port,
            database=dbdata.db_model_name)
        self.cursor = self.connection.cursor()

    def query(self,query,params):
        try:
            res = self.cursor.execute(query,params)
            self.connection.commit()
            return self.cursor.rowcount
        except (Exception, psycopg2.Error) as error :
            print("Error al ejecutar query -- ", error)
            return -1
    def query_many(self,query,p_list):
        try:
            res = self.cursor.executemany(query,p_list)
            self.connection.commit()
            return self.cursor.rowcount
        except (Exception, psycopg2.Error) as error :
            print("Error al ejecutar query -- ", error)
            return -1


    def fetch_one(self,query,p_list):
        try:
            res = self.cursor.execute(query,p_list)
            self.connection.commit()
            return self.cursor.fetchone()
        except (Exception, psycopg2.Error) as error :
            print("Error al ejecutar query -- ", error)
            return -1
    def fetch_all(self,query,p_list):
        try:
            res = self.cursor.execute(query,p_list)
            self.connection.commit()
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print("Error al ejecutar query -- ", error)
            return -1

    def __del__(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()