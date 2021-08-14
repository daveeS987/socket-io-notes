import socketio
from faker import Faker
from time import time, sleep

from socketio import client

fake = Faker("en_US")

sio = socketio.Client()


@sio.event
def connect():
    print("Client 4 connected")
    sio.emit("message_from_client", "from client4")


@sio.event
def my_message(data):
    print("message received with ", data)
    sio.emit("my response", {"response": "my response"})


@sio.event
def disconnect():
    print("disconnected from server")


# s = SocketConnections()
sio.connect("http://localhost:8000", namespaces=["/game"])

while True:
    sio.emit("move", fake.name(), namespace="/game")
    sleep(0.1)


# sio.wait()
# Nothing will run after sio.wait()
