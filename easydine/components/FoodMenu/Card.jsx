import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image } from 'react-native';
import React from 'react';
import { Button } from 'react-native';
export default function Card(props) {
    return (
      <View style={styles.container}>
        <View style={styles.info}>
            <Text>{props.name}</Text>
            <Text>Rate: {props.rate}</Text>
            <View style = {styles.add}><Button title="add" onPress={()=>props.addItem({name:props.name,rate:props.rate})}>Add</Button></View>
        </View>
        <Image 
        style={styles.image}
        source={{
          uri: props.image,
        }}/>
        
          
      </View>
    );
  }

const styles = StyleSheet.create({
    container:{
        padding: 0,
        flexDirection:'row',
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
      marginTop: 10,
      marginBottom: 10,
    },
    add:{
      width:100,
      backgroundColor:"blue"
    }
})