import socketio
from faker import Faker
from time import time, sleep

fake = Faker("en_US")

# -------------- Will trigger GameNameSpace in Server ----------
sio = socketio.Client()


@sio.event
def connect():
    print("Player 2 connected")
    sio.emit("message_from_client", "from client3")


@sio.event
def my_message(data):
    print("message received with ", data)
    sio.emit("my response", {"response": "my response"})


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://localhost:8000", namespaces=["/game"])


while True:
    sio.emit("move", fake.name(), namespace="/game")
    sleep(0.1)


# sio.wait()
# Nothing will run after sio.wait()
