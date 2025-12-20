from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat/<room>')
def chat(room):
    if room.lower() not in ['a', 'b', 'c', 'd']:
        return redirect(url_for('index'))
    return render_template('page1.html', room_id=room.upper())

@app.route('/settings')
def settings():
    return render_template('page2.html')

# --- SOCKETS ---

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    # emit('system_msg', {'msg': f'{username} joined.'}, to=room)

@socketio.on('message')
def handle_message(data):
    msg = data['msg']
    username = data['username']
    room = data['room']
    color = data.get('color', '#000000')
    
    # Capture the time the message arrived at server
    timestamp = time.time() 

    emit('chat_msg', {
        'username': username, 
        'msg': msg, 
        'color': color,
        'server_time': timestamp # Send this back to client
    }, to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)