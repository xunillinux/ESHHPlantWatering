from mysql import connector as mariadb
import json

class Repository:

    def __init__(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
    
    def AddHumidityValue(self, humidity_value = 0):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO humidity (humidity_value) VALUES (%s)", (humidity_value,))
        db_connection.commit()

    def GetHumidityValues(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("SELECT humidity_value, measure_date from humidity")
        return self.GetJsonResultFromCursor(cursor)
    

    def AddBrightnessValue(self, brightness_value = 0):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO brightness (brightness_value) VALUES (%s)", (brightness_value,))
        db_connection.commit()
    
    def GetBrightnessValues(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("SELECT brightness_value, measure_date from brightness")
        return self.GetJsonResultFromCursor(cursor)
    

    def AddTemperatureValue(self, temperature_value = 0):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO temperature (temperature_value) VALUES (%s)", (temperature_value,))
        db_connection.commit()
    
    def GetTemperatureValues(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("SELECT temperature_value, measure_date from temperature")
        return self.GetJsonResultFromCursor(cursor)
    

    def SetPhoto(self, photo_path = ""):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO photo (photo_path) VALUES (%s)", (photo_path,))
        db_connection.commit()

    def GetPhotos(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("SELECT photo_path, measure_date from photo")
        return self.GetJsonResultFromCursor(cursor)


    def SetSettings(self, humidity_threshhold = 250, pump_water_amount = 100):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM settings WHERE id=1")
        cursor.execute("INSERT INTO settings (id, humidity_threshhold, pump_water_amount) VALUES (%s,%s, %s)", (1, humidity_threshhold, pump_water_amount))
        db_connection.commit()

    def GetSettings(self):
        db_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
        cursor = db_connection.cursor()
        cursor.execute("SELECT humidity_threshhold, pump_water_amount from settings WHERE id=1")
        return self.GetJsonResultFromCursor(cursor)



    def GetJsonResultFromCursor(self, cursor):
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data, default=str)
