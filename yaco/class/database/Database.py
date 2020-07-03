import psycopg2
class PSConnection:
    def __init__(self):
        self.connection = psycopg2.connect(user="nico",password="postgres",host="127.0.0.1",port="5432",database="yaco")
        self.cursor = self.connection.cursor()

    def query(self,query,params):
        try:
            res = self.cursor.execute(query,params)
            self.connection.commit()
            return self.cursor.rowcount
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print("Error al insertar definicion ", error)
            return -1

    def __del__(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()