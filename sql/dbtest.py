#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
cursor = mariadb_connection.cursor()

cursor.execute("DELETE FROM settings WHERE id=1")
mariadb_connection.commit()

cursor.execute("INSERT INTO settings (id, humidity_threshhold, pump_water_amount) VALUES (%s,%s, %s)", (1, 42, 69))
mariadb_connection.commit()

cursor.execute("SELECT id, humidity_threshhold, pump_water_amount FROM settings WHERE id=1")

for id, humidity_threshhold, pump_water_amount in cursor:
    print("Id: {}, humidity threshhold: {}, water amount: {}").format(id, humidity_threshhold, pump_water_amount) 


cursor.execute("DELETE FROM settings WHERE id=1")

mariadb_connection.commit()

