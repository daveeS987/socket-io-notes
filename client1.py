import socketio
from time import time, sleep
import random


# -------------- Will trigger Global Namespace in Server ----------
sio = socketio.Client()


@sio.event
def connect():
    print("Player 1 Connected")
    sio.emit("message", "Player 1")


@sio.event
def message(data):
    print("Player1 Received Message:", data)
    sio.emit("my response", "A listener that was triggered by response")


@sio.event
def move(data):
    print("Player 1 Received Move: ", data)


@sio.event
def disconnect():
    print("Player 1 Disconnected from server")


sio.connect("http://localhost:8000")

while True:
    a_move = random.choice(["left", "right", "up", "down"])
    sio.emit(
        "move",
        a_move,
    )
    sleep(1)

# sio.wait()
