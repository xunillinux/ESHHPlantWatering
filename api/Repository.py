import mysql.connector as mariadb
import json

class Repository:

    def __init__(self):
        self.db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
    
    def SetHumidityValues():
        

    def GetHumidityValues():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT humidity_value, measure_date from humidity")
        return GetJsonResultFromCursor(cursor)
    
    def GetBrightnessValues():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT brightness_value, measure_date from brightness")
        return GetJsonResultFromCursor(cursor)
    
    def GetTemperatureValues():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT temperature_value, measure_date from temperature")
        return GetJsonResultFromCursor(cursor)
    
    def GetFotos():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT foto_path, measure_date from foto")
        return GetJsonResultFromCursor(cursor)

    def GetSettings():
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT humidity_threshhold, pump_water_amount from settings WHERE id=1")
        return GetJsonResultFromCursor(cursor)



    def GetJsonResultFromCursor():
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
