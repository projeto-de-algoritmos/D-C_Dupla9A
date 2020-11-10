from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from mergesort import mergesort

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('mergesort.html')

@socketio.on('start')
def handle_start(message):
    array = message['array']
    result = mergesort(array)
    socketio.emit('update', {'array': result})

if __name__ == '__main__':
    socketio.run(app)


