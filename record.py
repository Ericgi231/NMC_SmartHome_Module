import Adafruit_DHT
import mysql.connector
import json

sensor = Adafruit_DHT.DHT11
pin = 4

with open('config.json') as data_file:
	data = json.load(data_file)

userId = int(data["UserId"])
unitId = int(data["UnitId"])

humid, temp = Adafruit_DHT.read_retry(sensor, pin)

cnx = mysql.connector.connect(user='SmartUser', password='Password1', host='108.174.56.152', port='3306', database='SmartHome')

cur = cnx.cursor()
sql = "INSERT INTO Climate (Id, UserId, UnitId, Humidity, Temperature, RecordTime) VALUES (DEFAULT, %s, %s, %s, %s, DEFAULT)"
val = (userId, unitId, humid, temp)

cur.execute(sql, val)
cnx.commit()

cnx.close()
