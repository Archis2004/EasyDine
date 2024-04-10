import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, TouchableOpacity} from 'react-native';
import React, { useState, useEffect } from 'react'
import { FontAwesome5 } from '@expo/vector-icons';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { FIREBASE_AUTH } from '../config';
import { firebase } from '../config';

export default function Checkout({ route }) {
    const {cart,total} = route.params;
 const [user, setUser] = useState(null);
 const [credits, setCredits] = useState(0);
 const [loading, setLoading] = useState(true);
 const memRef = firebase.firestore().collection('Members');

const handleCredits = (newAmount)=>{

}

const handleGPay = ()=>{

}

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

  return(
    <View>
        <View style={styles.priceContainer}>
        <Text style={styles.label}>Amount to be paid: </Text>
        <Text style={styles.amount}>{total}</Text>
        <Text style={styles.label}> Current Balance: </Text>
        <Text style={styles.amount}>{credits}</Text>
        </View>
        <Text style={styles.optiontext}>Payment options:</Text>
    <View style={styles.paymentContainer}>
        <TouchableOpacity style={styles.paymentOption} onPress={()=>handleCredits(credits-total)}>
        <FontAwesome5 name="coins" size={24} color="black"/>

        </TouchableOpacity>
        <TouchableOpacity style={styles.paymentOption} onPress={handleGPay}>
        <FontAwesome5 name="google-pay" size={24} color="black" />

        </TouchableOpacity>
    </View>
    </View>
    
  )
}

const styles = StyleSheet.create({
    priceContainer:{
        backgroundColor:"white",
        margin:20,
        borderRadius: 10,
        alignItems: "center",
        padding: 10,
        marginBottom: 60,
    },
    amount:{
        fontSize:50,
        fontWeight:"600",
        color: "#4960F0",
    },
    label:{
        fontSize:20,
    },
    paymentOption:{
        flexDirection:"row",
        backgroundColor:"white",
        margin:5,
        borderRadius: 10,
        justifyContent: "center",
        height:70,
        alignItems:"center",
        width: 180,
    },
    optiontext:{
        marginLeft:30,
        marginBottom:30,
        fontWeight:"500",
        fontSize:16,
        color: "gray"
    },
    paymentContainer:{
        flexDirection:"row",
        justifyContent:"space-around",
    }
})