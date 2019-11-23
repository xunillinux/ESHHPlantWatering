import mysql.connector as mariadb
import json

class Repository:

    def __init__(self):
        self.db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
    
    def GetHumidityValues():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT value, timestamp from humidity")
        return GetJsonResultFromCursor(cursor)
    
    def GetJsonResultFromCursor():
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
