import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit.components.v1.custom_component






import streamlit as st
import streamlit.components.v1


from utilities import get_app_logger, get_file_path
from ign.mysecrets import SPOTIFY_CLIENT_ID, SPOTIFY_SECRET
from consts import SPOTIFY_REDIRECT_URI
from streamlit_js_eval import streamlit_js_eval

# Scopes for the Spotify API
scope = "user-read-private user-read-email"



sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
)

# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()



st.markdown("<span>Hello")
st.html("<a href='www.google.com'</a>")
st.html('<link rel="javascript" href="https://www.gstatic.com/_/mss/boq-one-google/_/js/k=boq-one-google.OneGoogleWidgetUi.de.l8rqCgWzmrY.es5.O/ck=boq-one-google.OneGoogleWidgetUi.OUuozmK6qro.L.F4.O/am=FAiAAbYB/d=1/exm=A7fCU,BVgquf,EFQ78c,GkRiKb,IZT63,IkEnFc,JNoxi,KUM7Z,L1AAkb,LEikZe,LvGhrf,MI6k7c,MdUzUe,MpJwZc,NwH0H,O1Gjze,O6y8ed,ORlaSe,OTA3Ae,PrPYRd,QIhFr,RMhBfe,RqjULd,RyvaUb,SdcwHb,SpsfSb,UUJqVe,Uas9Hd,Ujeq8,Ulmmrd,V3dDOb,XVMNvd,Z5uLle,ZDZcre,ZwDk9d,_b,_tp,aW3pY,byfTOb,e5qFLc,gychg,hKSk3e,hc6Ubd,kjKdXe,lazG7b,lsjVmc,lwddkf,mI3LFb,mdR7q,n73qwf,noLxJb,p3hmRc,pjICDe,pw70Gc,s39S4,w9hDv,wmnU7d,ws9Tlc,xQtZb,xUdipf,zbML3c,zr1jrb/excm=_b,_tp,appwidgetauthview/ed=1/wt=2/ujg=1/rs=AM-SdHuVGDShVtKMGHcrIxdLpkVwZkXCGw/ee=EVNhjf:pw70Gc;EmZ2Bf:zr1jrb;JsbNhc:Xd8iUd;K5nYTd:ZDZcre;LBgRLc:SdcwHb;Me32dd:MEeYgc;NPKaK:SdcwHb;NSEoX:lazG7b;Pjplud:EEDORb;QGR0gd:Mlhmy;SNUn3:ZwDk9d;ScI3Yc:e7Hzgb;Uvc8o:VDovNc;YIZmRd:A1yn5d;a56pNe:JEfCwb;cEt90b:ws9Tlc;dIoSBb:SpsfSb;dowIGb:ebZ3mb;eBAeSb:zbML3c;iFQyKf:QIhFr;lOO0Vd:OTA3Ae;nAFL3:s39S4;oGtAuc:sOXFj;pXdRYb:MdUzUe;qafBPd:yDVVkb;qddgKe:xQtZb;wR5FRb:O1Gjze;xqZiqf:wmnU7d;yxTchf:KUM7Z;zxnPse:GkRiKb/m=sOXFj,q0xTif,IiCRgf">')
st.markdown("<iframe src=\"https://www.google.com\"", unsafe_allow_html=True)
get_app_logger().info("Hola")
st.markdown(f"<script>console.log('Hi there')</script>", unsafe_allow_html=True)
st.markdown("<iframe><html><body><span>Hier </span></body></html></iframe>", unsafe_allow_html=True)
streamlit.components.v1.iframe(src=auth_url, width=400, height=400, scrolling=True)



import requests

# Dein Hugging Face API Token
API_TOKEN = "hf_XXXXXXXXXXXXXXXXXXXX"

# Das gewünschte TTS Modell
MODEL_NAME = "espnet/kan-bayashi_ljspeech_vits"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = API_TOKEN
# Text, der in Sprache umgewandelt werden soll
text = "Hallo! Dies ist eine Sprachausgabe mit Hugging Face."

# Anfrage an die Hugging Face API senden
def text_to_speech(text):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": text
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        with open("output.wav", "wb") as f:
            f.write(response.content)
        print("Sprachdatei wurde gespeichert als 'output.wav'.")
    else:
        print(f"Fehler {response.status_code}: {response.text}")

# Funktion aufrufen
text_to_speech(text)



