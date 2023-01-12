import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import pyrebase

i2c = board.I2C() 
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")


while True:
    temperature_c = "{:.2f}".format(bme280.temperature)
    humidity = "{:.2f}".format(bme280.relative_humidity)
    
    temp = float(temperature_c)
    hum = float(humidity)
    
    print("Temperature: {} °C" .format(temperature_c))
    print("Humidity: {}" .format(humidity))
			
    data = {
    "Temperature" : temp,
    "Humidity" : hum,
    }
    db.child("bme280").child("Temperature").set(data["Temperature"])
    db.child("bme280").child("Humidity").set(data["Humidity"])
        
    print("Sent to Firebase")
        
    time.sleep(0.5)


