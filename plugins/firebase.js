import * as firebase from 'firebase/app'
import 'firebase/auth'

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyApeboHEWeZRrO3UNJQG425uNr3SUZzkT4',
  authDomain: 'corpad-ee943.firebaseapp.com',
  databaseURL: 'https://corpad-ee943.firebaseio.com',
  projectId: 'corpad-ee943',
  storageBucket: 'corpad-ee943.appspot.com',
  messagingSenderId: '403838723221',
  appId: '1:403838723221:web:e5cd5a38c497d1fab7a79c',
  measurementId: 'G-RRB9FNW4Y8',
}

let app = null
if (!firebase.apps.length) {
  app = firebase.initializeApp(firebaseConfig)
}
// Initialize Firebase

// firebase.analytics()

export default firebase
