import { View, Text, FlatList, StyleSheet, Pressable } from 'react-native'
import React, { useState, useEffect } from 'react'
import { firebase } from '../../config';

const Fetch = () => { 

    const [itemss, setItemss] = useState([]);
    const orderRef = firebase.firestore().collection('Orders');

    useEffect(() => { 
        async function fetchData() {
            orderRef
            .onSnapshot(
                querySnapshot => {
                    const items = []
                    querySnapshot.forEach((doc) => { 
                        const { items, total } = doc.data()
                        items.push({
                            id: doc.id,
                            items,
                            total,
                        })
                    })
                    setItemss(itemss)
                }
            )
        }
        fetchData();
    }, [])

    return (itemss)
}

export default Fetch

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