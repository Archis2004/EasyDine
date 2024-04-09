import { View, Text, FlatList, StyleSheet, Pressable } from 'react-native'
import React, { useState, useEffect } from 'react'
import { firebase } from '../../config';

const FetchBV = () => { 

    const [items, setItems] = useState([]);
    const menuRef = firebase.firestore().collection('Menu');
    const breakfastRef = menuRef.doc('Breakfast');
    const vegBfRef = breakfastRef.collection('Veg');

    useEffect(() => { 
        async function fetchData() {
            vegBfRef
            .onSnapshot(
                querySnapshot => {
                    const items = []
                    querySnapshot.forEach((doc) => { 
                        const { name, quantity, rate } = doc.data()
                        items.push({
                            id: doc.id,
                            name,
                            quantity,
                            rate,
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

export default FetchBV

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