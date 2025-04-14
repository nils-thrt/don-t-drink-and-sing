from flask import Flask, jsonify, render_template
from google.cloud import firestore
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@cross_origin()
@app.route("/login")
def home():
    return jsonify({"message": "Hello World!"})


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