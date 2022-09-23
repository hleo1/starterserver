import pymysql
import os



class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get('DBUSER')
        pw = os.environ.get('DBPW')
        h = os.environ.get('DBHOST')

        conn = pymysql.connect(
            user= 'admin',
            password= 'butterfly55',
            host= 'database-1.co4esxmwwvi8.us-east-1.rds.amazonaws.com',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM cloudcomputingstarter.columbia_students where school_code=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

