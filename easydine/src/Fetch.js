import { View, Text, FlatList, StyleSheet, Pressable } from 'react-native'
import React, { useState, useEffect } from 'react'
import { firebase } from '../config';
import { QuerySnapshot } from 'firebase/firestore';

const Fetch = () => { 

    const [users, setUsers] = useState([]);
    const menuRef = firebase.firestore().collection('Menu');
    const breakfastRef = menuRef.doc('Breakfast');
    const vegBfRef = breakfastRef.collection('Veg');

    useEffect(async () => { 
        vegBfRef
        .onSnapshot(
            querySnapshot => {
                const users = []
                querySnapshot.forEach((doc) => { 
                    const { name, quantity, rate } = doc.data()
                    users.push({
                        id: doc.id,
                        name,
                        quantity,
                        rate,
                    })
                })
                setUsers(users)
            }
        )
    }, [])

    return (
        <View style={{ flex: 1, marginTop: 100 }}>
            <FlatList>
                style={{ height: '100%' }}
                data={users}
                numColumns={1}
                renderItem = {({ item }) => (
                    <Pressable
                        // style={StyleSheet.container}
                    >
                        <View stle={StyleSheet.innerContainer}>
                            <Text>{item.name}</Text>
                            <Text>{item.quantity}</Text>
                            <Text>{item.rate}</Text>
                        </View>
                    </Pressable>
                )}
            </FlatList>
        </View>
    )
}

export default Fetch