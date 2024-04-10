import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { firebase } from '../config';

export default function Credits() {
  const [user, setUser] = useState(null);
  const [credits, setCredits] = useState(0);
  const [loading, setLoading] = useState(true);
  const memRef = firebase.firestore().collection('Members');

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(getAuth(), (user) => {
      setUser(user);
    });

    return unsubscribe;
  }, []);

  useEffect(() => {
    if (!user) return; // No need to fetch if there's no user

    const fetchData = async () => {
      try {
        const snapshot = await memRef.where('regno', '==', user.email.slice(0, -10).toUpperCase()).get();
        if (!snapshot.empty) {
          const doc = snapshot.docs[0];
          setCredits(doc.data().credits || 0);
        }
      } catch (error) {
        console.error('Error fetching credits:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [user]);

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <Text>Loading...</Text>
      </View>
    );
  }

  const now = new Date();
  const days = now.getDate();
  console.log(credits);
  const firstDayOfNextMonth = new Date(now.getFullYear(), now.getMonth() + 1, 1);
  const lastDayOfCurrentMonth = new Date(firstDayOfNextMonth - 1);
  const daysInMonth = lastDayOfCurrentMonth.getDate();

  return (
    <View style={styles.outer}>
      <View style={styles.current}>
        <Text style={styles.label}>Current Credits: </Text>
        <Text style={styles.amount}>{credits}</Text>
      </View>

      <View style={styles.current}>
          <Text style={styles.label}>Credits Spent per day:</Text>
        <Text style={styles.amount}>{(Math.floor((6180 - credits)/days))}</Text>
      </View>
          
      <View style={styles.current}>
          <Text style={styles.label}>Credits Remaining per day:</Text>
        <Text style={styles.amount}>{(Math.floor(credits/ (daysInMonth - days)))}</Text>
      </View>
    </View>
    
  );
}

const styles = StyleSheet.create({
  outer: {
    flex: 1,
    backgroundColor: '#F8F6E3',
    padding: 20,
  },
  current: {
    borderRadius: 20,
    backgroundColor: '#C4E4FF',
    padding: 20,
    marginBottom: 20,
  },
  label: {
    fontSize: 20,
    color: '#000FFF',
  },
  amount: {
    fontSize: 70,
    fontWeight: '400',
    color: '#000FFF',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});