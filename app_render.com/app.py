from flask import Flask, jsonify, render_template
from google.cloud import firestore
from flask_cors import CORS, cross_origin
from spotipy.oauth2 import SpotifyOAuth

from ign.spotify_secrets import SPOTIFY_CLIENT_ID, SPOTIFY_SECRET

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri="http://localhost:4200/spotify-callback",
    scope="user-read-private user-read-email"
    
)



    



@app.route("/login")
def home():
    return jsonify({"message": "Hello World!"})

@app.route("/getSpotifyAuthorizationLink")
def getSpotifyAuthorizationLink():

    authorizationUrl = 'https://accounts.spotify.com/authorize?'
    authorizationUrl += "response_type=code"
    authorizationUrl += "&client_id=" + SPOTIFY_CLIENT_ID
    authorizationUrl += "&scope=user-read-private+user-read-email+streaming"
    authorizationUrl += "&redirect_uri=http://localhost:4200/spotify-callback"

    return jsonify({"link": authorizationUrl})



@app.route("/requestAccessToken/{resp_code}", methods=["POST"])
def requestAccessToken():

    sp_oauth.get_access_token(as_dict=True)
    authorizationUrl = 'https://accounts.spotify.com/authorize?'
    authorizationUrl += "response_type=code"
    authorizationUrl += "&client_id=" + SPOTIFY_CLIENT_ID
    authorizationUrl += "&scope=user-read-private+user-read-email"
    authorizationUrl += "&redirect_uri=http://localhost:4200/spotify-callback"

    return jsonify({"link": authorizationUrl})






@app.after_request
def set_response_headers(response):
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, Access-Control-Allow-Header,  Access-Control-Allow-Origin, Access-Control-Allow-Credentials, X-Requested-With, Accept"
    return response


""" # Optional: Wenn du das Skript außerhalb der GCP-Umgebung ausführst
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/etc/secrets/firebase-adminsdk.json"

# Firestore-Client initialisieren
db = firestore.Client() """

""" # Beispiel: Dokument in einer Collection speichern
doc_ref = db.collection("users").document("max")
doc_ref.set({
    "name": "Max Mustermann",
    "email": "max@example.com"
}) """
""" 
# Beispiel: Dokument lesen
doc = doc_ref.get()
if doc.exists:
    print("Dokumentdaten:", doc.to_dict())
else:
    print("Kein solches Dokument.")


 """