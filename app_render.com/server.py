from flask import Flask, request, jsonify, make_response
#from flask_cors import CORS
import random
import string
from TTS.api import TTS

app = Flask(__name__)
#CORS(app)

# Initialize the Coqui TTS engine
tts = TTS()

# Store session data in a dictionary for simplicity
sessions = {}

@app.route('/create_session', methods=['POST'])
def create_session():
    name = request.json['name']
    session_id = generate_session_id()
    sessions[session_id] = {'host': name, 'joined_users': [], 'song_queue': []}
    resp = make_response(jsonify({'session_id': session_id}), 200)
    resp.set_cookie('SESSION_ID', session_id, secure=True, samesite='None')
    return resp


@app.route('/join_session', methods=['POST'])
def join_session():
    session_id = request.json['session_id']
    name = request.json['name']
    if session_id in sessions:
        sessions[session_id]['joined_users'].append(name)
        return jsonify({'message': 'Joined session successfully'})
    else:
        return jsonify({'error': 'Invalid session ID'}), 400


@app.route('/add_song', methods=['POST'])
def add_song():
    session_id = request.json['session_id']
    song_uri = request.json['song_uri']
    user_name = request.json['user_name']
    if session_id in sessions:
        # Generate the intro TTS audio
        audio_file = generate_tts_audio(user_name, song_uri)
        # Add the song to the queue
        sessions[session_id]['song_queue'].append({'song_uri': song_uri, 'audio_file': audio_file})
        return jsonify({'message': 'Song added to queue successfully'})
    else:
        return jsonify({'error': 'Invalid session ID'}), 400


def generate_session_id():
    # Generate a random 10-character session ID
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def generate_tts_audio(user_name, song_uri):
    # Generate the intro TTS audio using Coqui TTS
    text = f"Now playing {song_uri} from {user_name}"
    audio_file = tts.say(text)
    return audio_file


if __name__ == '__main__':
    app.run(debug=True)