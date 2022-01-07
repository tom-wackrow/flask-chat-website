from app import socketio
from flask_socketio import join_room, leave_room
from flask_login import current_user


@socketio.on('join', namespace='/room')
def join(message):
    room = current_user.room
    join_room(room, namespace="/room")
    socketio.emit("message", message, room=room, namespace="/room")


@socketio.on('message', namespace='/room')
def handle_message(message):
    room = current_user.room
    socketio.emit("message", message, room=room, namespace="/room")

@socketio.on("disconnect", namespace="/room")
def disconnect(message):
    room = current_user.room
    leave_room(room)
    current_user.room = None
    disconnect()