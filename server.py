from flask import Flask
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'm11.cloudmqtt.com'
app.config['MQTT_BROKER_PORT'] = 11730
app.config['MQTT_USERNAME'] = 'ctanobuc'
app.config['MQTT_PASSWORD'] = 't2c73UnIQwOh'
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt()
