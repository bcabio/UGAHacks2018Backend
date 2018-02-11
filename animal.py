import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe

broker_address = "m11.cloudmqtt.com"
port = 11730
user = "ctanobuc"
password = "t2c73UnIQwOh"

def on_message(mosq, obj, msg):
    print(msg.topic, msg.qos, msg.payload)
    print('lel')

if __name__ == '__main__':
    client = paho.Client()
    client.username_pw_set(user, password=password)
    client.on_message = on_message
    

    client.connect(broker_address, port=port)

    client.subscribe("ugahacks/brian", 0)

    client.loop_forever()
