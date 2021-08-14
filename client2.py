import socketio
from time import time, sleep
import random


# -------------- Will trigger Global Namespace in Server ----------
sio = socketio.Client()


@sio.event
def connect():
    print("Player 2 Connected")
    sio.emit("message", "Player 2")


@sio.event
def message(data):
    print("Player2 Received Message:", data)
    sio.emit("my response", "A listener that was triggered by response")


@sio.event
def move(data):
    print("Player 2 Received Move: ", data)


@sio.event
def disconnect():
    print("Player 2 Disconnected from server")


sio.connect("http://localhost:8000")

while True:
    a_move = random.choice(["2LEFT", "2RIGHT", "2UP", "2DOWN"])
    sio.emit(
        "move",
        a_move,
    )
    sleep(2)

# sio.wait()
