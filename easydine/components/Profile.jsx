import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Button } from 'react-native';
import React, { useState, useEffect } from 'react'
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { FIREBASE_AUTH } from '../config';
import { firebase } from '../config';

export default function Profile() {

  const [user, setUser] = useState(null);
  
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(FIREBASE_AUTH, (user) => {
      setUser(user);
      if (user) {
        console.log(user.email.slice(0,-10).toUpperCase());
      }
    });

    return () => unsubscribe();
  }, []);

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      {user && <Text>Reg No: {user.email.slice(0,-10).toUpperCase()}</Text>}
      <Button onPress={() => FIREBASE_AUTH.signOut()} title='LogOut' />
    </View>
  );
}