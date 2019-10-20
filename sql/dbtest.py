#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='dbuser', password='Welcome$16', database='plantwateringdb')
cursor = mariadb_connection.cursor()

cursor.execute("INSERT INTO pumpsettings (id,water_amount) VALUES (%s,%s)", (1, 42))

mariadb_connection.commit()

cursor.execute("SELECT id,water_amount FROM pumpsettings WHERE id=1")


for id, water_amount in cursor:
    print("Id: {}, water amount: {}").format(id, water_amount) 


cursor.execute("DELETE FROM pumpsettings WHERE id=1")

mariadb_connection.commit()

