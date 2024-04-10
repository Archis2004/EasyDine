import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { firebase } from '../config';

export default function Orders() {
  const [user, setUser] = useState(null);
  const [orders, setOrders] = useState(0);
  const [itemss, setItemss] = useState([]);
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
          console.log(' ');
          console.log(memRef.doc(`{doc.data().regno}`).collection('Transactions'));
          const bruh = memRef.doc(`{doc.data().regno}`).collection('Transactions');
          const gg = bruh.doc('1');
          console.log(gg.data().to_dict);
          bruh
            .onSnapshot(
                querySnapshot => {
                    const itemss = []
                    querySnapshot.forEach((doc) => { 
                        const { items, price, time } = doc.data()
                        itemss.push({
                          items,
                          price,
                          time,
                        })
                    })
                    setItemss(itemss)
                }
            )
          console.log(itemss);
          
          setOrders(doc.data().orders || 0);
        }
      } catch (error) {
        console.error('Error fetching past orders:', error);
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


  return (
    <View style={styles.outer}>
      <View style={styles.current}>
        <Text style={styles.label}>Current Credits: </Text>
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