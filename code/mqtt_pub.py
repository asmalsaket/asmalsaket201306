import paho.mqtt.client as mqtt
import json

broker_address="10.20.1.95"
#Publisher
client = mqtt.Client()
topic = "se443/midterm2"
message = '{ "StudentID": 201306,"Name":"Asma", "Surname":"Alsaket", "Telephone":"057777777", "Grade":99}'
if (client.connect(broker_address,1883,60) ==0):
	print ("Connected succesfully to "+broker_address)
	
client.publish(topic, message)
print ("Published in "+topic+", msg = "+message)
client.disconnect();