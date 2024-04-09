import { View, Text, FlatList, StyleSheet, Pressable } from 'react-native'
import React, { useState, useEffect } from 'react'
import { firebase } from '../../config';

const FetchLV = () => { 

    const [items, setItems] = useState([]);
    const menuRef = firebase.firestore().collection('Menu');
    const lunchRef = menuRef.doc('Lunch');
    const VegLunRef = lunchRef.collection('Veg');

    useEffect(() => { 
        async function fetchData() {
            VegLunRef
            .onSnapshot(
                querySnapshot => {
                    const items = []
                    querySnapshot.forEach((doc) => { 
                        const { name, quantity, rate, image } = doc.data()
                        items.push({
                            id: doc.id,
                            name,
                            quantity,
                            rate,
                            image,
                        })
                    })
                    setItems(items)
                }
            )
        }
        fetchData();
    }, [])

    return (items)
}

export default FetchLV

const styles = StyleSheet.create({
    conainter: {
        backgroundColor: 'e5e5e5',
        padding: 15,
        borderRadius: 15,
        margin: 5,
        marginHorizontal:10,
    },
    innerContainer:{
        alignItems: 'center',
        flexDirection:'column',
    },
    itemName: {
        fontWeight:'bold'
    },
    iitemQty: {
        fontWeight:'300'
    },
    itemRate: {
        fontWeight:'300'
    },
})