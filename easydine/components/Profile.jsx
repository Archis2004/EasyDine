import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Button, TouchableOpacity } from 'react-native';
import React, { useState, useEffect } from 'react'
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { FIREBASE_AUTH } from '../config';
import { firebase } from '../config';

export default function Profile() {

  const [user, setUser] = useState(null);
  const [fname, setFname] = useState('');
  const [lname, setLname] = useState('');
  const memRef = firebase.firestore().collection('Members');

  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(FIREBASE_AUTH, (user) => {
      setUser(user);
      console.log(user);
      if (user) {
        console.log(user.email.slice(0,-10).toUpperCase());
      }
    });
    return () => unsubscribe();
  }, []);

  useEffect(() => {
    if (!user) return; // No need to fetch if there's no user

    const fetchData = async () => {
      try {
        const snapshot = await memRef.where('regno', '==', user.email.slice(0, -10).toUpperCase()).get();
        if (!snapshot.empty) {
          const doc = snapshot.docs[0];
          setFname(doc.data().fname);
          setLname(doc.data().lname);
        }
      } catch (error) {
        console.error('Error fetching credentials:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [user]);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={style.greeting}>Welcome!</Text>
      {user && <Text style={{ margin: 5, fontSize: 35,fontWeight:"700" }}> {fname} { lname}</Text>}
      {user && <Text style={{ margin: 10, fontSize: 25 }}>Reg No: {user.email.slice(0, -10).toUpperCase()}</Text>}
      <TouchableOpacity style={style.logout} onPress={() => FIREBASE_AUTH.signOut()}>
        <Text style={style.logtext}>Logout</Text>
      </TouchableOpacity>
    </View>
  );
}

const style = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  text: {
    margin: 15,
    fontSize: 100,
  },
  greeting:{
    fontSize: 25,
    marginBottom:10,
    
  },
  logout: {
    backgroundColor: "#2A3CD5",
    height: 40,
    justifyContent: "center",
    alignItems: "center",
    width: 150,
    borderRadius:10,
    marginTop: 20,
  },
  logtext: {
    color: "white",
    fontWeight:"700"
  }
})