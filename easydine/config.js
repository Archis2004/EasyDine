import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore'
import ReactNativeAsyncStorage from '@react-native-async-storage/async-storage';
import { initializeApp,  } from 'firebase/app'
import { getAuth, initializeAuth, getReactNativePersistence } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyCUO2tMlQnuhZZXVwdFH5adbzOGR2QexQ0",
  authDomain: "food-park-easydine.firebaseapp.com",
  projectId: "food-park-easydine",
  storageBucket: "food-park-easydine.appspot.com",
  messagingSenderId: "327120657471",
  appId: "1:327120657471:web:5ced14ff15101d9eca6c8a",
  measurementId: "G-QLQ8LP4PS2"
};

if (!firebase.apps.length) { 
    firebase.initializeApp(firebaseConfig)
}

export { firebase };
export const FIREBASE_APP = initializeApp(firebaseConfig);
export const FIREBASE_AUTH = getAuth(FIREBASE_APP, {persistence: getReactNativePersistence(ReactNativeAsyncStorage)});