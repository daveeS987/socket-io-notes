# run this in the terminal to start server
# >>>>>> gunicorn --threads 50 server:app
# ----------------------------------
# the code about uses gunicorn to start the server
# it uses 50 threads
# nameOfFile : the app variable
import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio)

# this is a built in listener given to us by socketio
@sio.event
def connect(sid, environ):
    print("A new Player connected to global namespace", sid)
    sio.enter_room(sid, "game room")
    print("A new player entered game room")


# event listener
@sio.event
def move(sid, data):
    print("MOVE from client: ", data)
    sio.emit("move", data, room="game room", skip_sid=sid)


# this is another way to listen
@sio.event
def message(sid, data):
    print("MESSAGE from client: ", data)


# this is a built in listener given to us by socketio
@sio.event
def disconnect(sid):
    print("Disconnected SID >> ", sid)


# ---------------- Class Based NameSpace ------------
# this is a way to put a namespace into its own class
# You dont have to put it in its own class


# class GameNameSpace(socketio.Namespace):
#     def on_connect(self, sid, environ):
#         print("This is environ: ", environ)
#         print("--------------------------------")
#         print("A new client CONNECTed to game Namespace with ID: ", sid)

#     def on_message_from_client(self, sid, data):
#         print("Data from client intialize game: ", data)

#     def on_initialize_game(self, sid, data):
#         print("Data from client intialize game: ", data)

#     def on_disconnect(self, sid, data):
#         print("A client disconnected with ID: ", sid)

#     def on_move(self, sid, data):
#         print("GAME NAMESPACE MOVE: ", data)


# When using class based namespace, need to register is like this
# sio.register_namespace(GameNameSpace("/game"))


# ---------- Another way to do namespace --------------


# @sio.event(namespace="/chat")
# def my_custom_event(sid, data):
#     pass


# @sio.on("my custom event", namespace="/chat")
# def my_custom_event(sid, data):
#     pass
