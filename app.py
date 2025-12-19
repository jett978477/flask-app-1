from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    msg = data['msg']
    username = data['username']

    # Command Logic
    if msg.startswith('/'):
        command = msg.split(' ')[0].lower()
        
        if command == '/help':
            emit('system_msg', {'msg': 'Commands: /help, /ping, /name [newname]'})
        elif command == '/ping':
            emit('system_msg', {'msg': 'Pong!'})
        elif command == '/name':
            new_name = msg.split(' ', 1)[1] if ' ' in msg else "Anonymous"
            emit('system_msg', {'msg': f'System: Changing name to {new_name}'})
            emit('change_name', {'new_name': new_name})
        else:
            emit('system_msg', {'msg': 'Unknown command. Type /help.'})
    else:
        # Normal chat broadcast to everyone
        emit('chat_msg', {'username': username, 'msg': msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)