from app import socketio


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on("join")
def handle_connect(json, methods=["GET", "POST"]):
    print(f"<{json['user_name']}> {json['message']}")
    socketio.emit("message", json)

@socketio.on("message")
def handle_message(json, methods=["GET", "POST"]):
    print(f"<{json['user_name']}> {json['message']}")
    socketio.emit('message', json, callback=messageReceived)