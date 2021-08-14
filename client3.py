import socketio
from faker import Faker
from time import time, sleep

from socketio import client

fake = Faker("en_US")

sio = socketio.Client()


class SocketConnection(socketio.ClientNamespace):
    def on_connect(self):
        print("Connected to Server")
        self.emit("initialize_game", "player has connected", namespace="/game")

    def on_move_event(self, data):
        self.emit("my_response", data)

    def on_disconnect(self, sid, data):
        print("Client has Disconnected")

    def move(self, the_move):
        # print("the_move: ", the_move)
        self.emit("move", the_move)


sio.register_namespace(SocketConnection("/game"))
sio.connect("http://localhost:8000")

s = SocketConnection()

while True:
    s.move(fake.name())
    sleep(0.1)

sio.wait()
# Nothing will run after sio.wait()
