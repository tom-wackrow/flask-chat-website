from werkzeug.utils import redirect
from app import socketio
from flask_socketio import join_room, leave_room
from flask_login import current_user
from flask import redirect

@socketio.on('join', namespace='/room')
def join(message):
    if current_user.room == None:
        return redirect("index.html")
    room = current_user.room
    join_room(room, namespace="/room")
    socketio.emit("message", message, room=room, namespace="/room")


@socketio.on('message', namespace='/room')
def handle_message(message):
    if message["message"] == "":
        pass
    room = current_user.room
    socketio.emit("message", message, room=room, namespace="/room")

@socketio.on("disconnect", namespace="/room")
def disconnect():
    if current_user.room == None:
        return redirect("index.html")
    room = current_user.room
    leave_room(room)
    current_user.room = None
    disconnect()