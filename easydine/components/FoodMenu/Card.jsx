import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image } from 'react-native';
import React from 'react';
import { Button } from 'react-native';
export default function Card() {
    let data=[1,2,3,4,5,6]

    return (
      <View style={styles.container}>
        <View style={styles.info}>
            <Text>Dal Makhani</Text>
            <Text>Rate: 50</Text>
            <Button title="add">Add</Button>
        </View>
        <Image 
        style={styles.image}
        source={require('../../assets/Daal-Makhani-1-850x1275.webp')}/>
        
          
      </View>
    );
  }

const styles = StyleSheet.create({
    container:{
        padding: 0,
        flexDirection:'row',
        height: '25%',
        width: '100%', 
        overflow: "hidden",
        backgroundColor: "white",
        justifyContent: "space-between",
        alignItems: 'center',
        marginTop: 10,
    },
    image:{
        width:"40%", 
        height:"90%",
        marginRight: 10,
        borderRadius: 10,
    },
    info:{
        marginLeft: 20,
    }
})