import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import RPi.GPIO as GPIO
import time

broker_address = "m11.cloudmqtt.com"
port = 11730
user = "ctanobuc"
password = "t2c73UnIQwOh"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


def on_message(mosq, obj, msg):
    print(msg.topic, msg.qos, msg.payload)
    
    if int(msg.payload) == -1:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
 
    if int(msg.payload) >= 1:
        GPIO.output(18, GPIO.HIGH) 
    if int(msg.payload) >= 2:
        GPIO.output(27, GPIO.HIGH)
    if int(msg.payload) >= 3:
        GPIO.output(23, GPIO.HIGH)
    if int(msg.payload) >= 4:
        GPIO.output(24, GPIO.HIGH)
        
        for x in range(15):
            GPIO.output(18, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            time.sleep(.5)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            time.sleep(.5)

if __name__ == '__main__':

    client = paho.Client()
    client.username_pw_set(user, password=password)
    client.on_message = on_message
    

    client.connect(broker_address, port=port)

    client.subscribe("ugahacks/brian", 0)
    client.subscribe("reset", 0)
    client.loop_forever()
