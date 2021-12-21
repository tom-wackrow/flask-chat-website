from app import socketio
from flask_socketio import join_room, leave_room
from flask_login import current_user


@socketio.on('join', namespace='/room/<room_id>')
def join(message):
    room = current_user.current_room
    join_room(room)
    socketio.emit('status', {'message':  current_user.username + ' has entered the room.'}, room=room)


@socketio.on('message', namespace='/room/<room_id>')
def handle_message(message):
    room = current_user.current_room
    socketio.emit('message', {"user_name": current_user.username, 'message': current_user.username + ' : ' + message['message']}, room=room)