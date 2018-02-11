import os
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
from flask import Flask, request
from pymongo import MongoClient

web_port = int(os.environ.get('PORT', 5000))

broker_address = "m11.cloudmqtt.com"
port = 11730
user = "ctanobuc"
password = "t2c73UnIQwOh"

db_url = 'mongodb://admin:admin@ds231658.mlab.com:31658/ugahacks2018-mongo'
mongo_client = MongoClient(db_url)
db = mongo_client['ugahacks2018-mongo']

user_drinks = db['users']

app = Flask(__name__)

database = dict()

@app.route('/', methods=['GET'])
def goodbye():
#    client.publish('ugahacks/brian', request.args.get('pokemon'))
    return 'i did it'

@app.route('/', methods=['POST'])
def hello():
    print(request.args.get('person'))
    person_name = request.form.get('person')
    doc_cursor = user_drinks.update_one({}, {'$inc': {person_name: 1}})     
    database[person_name] += 1
    print('ugahacks/' + str(person_name.lower()))
    client.publish('ugahacks/' + str(person_name.lower()), database[person_name])
    print('here')
    return 'did it'

def on_connect(client, userdata, flags, rc):
    print('Connected with status ' + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic, msg.qos, msg.payload)
    print('lel')

if __name__ == '__main__':
    database['Brian'] = 0
    database['Aska'] = 0
    database['Shubham'] = 0
    database['David'] = 0

    client = paho.Client()
    client.username_pw_set(user, password=password)
    client.on_message = on_message
    client.connect(broker_address, port=port)
    client.loop_start()
    app.run(port=web_port)
