// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

import firebaseConfig from "./ign/config.js"

// Initialize Firebase
const app = initializeApp(firebaseConfig);


console.log("Firebase initialized");



// Firestore-Referenz holen
const db = firebase.firestore();

// Beispiel: Daten schreiben
db.collection("users").doc("user1").set({
  username: "Max",
  email: "max@example.com"
});
