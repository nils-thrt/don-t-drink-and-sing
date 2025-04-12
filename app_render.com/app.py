from flask import Flask, render_template
from google.cloud import firestore

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("html/index.html")




# Optional: Wenn du das Skript außerhalb der GCP-Umgebung ausführst
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/etc/secrets/firebase-adminsdk.json"

# Firestore-Client initialisieren
db = firestore.Client()

# Beispiel: Dokument in einer Collection speichern
doc_ref = db.collection("users").document("max")
doc_ref.set({
    "name": "Max Mustermann",
    "email": "max@example.com"
})

# Beispiel: Dokument lesen
doc = doc_ref.get()
if doc.exists:
    print("Dokumentdaten:", doc.to_dict())
else:
    print("Kein solches Dokument.")
