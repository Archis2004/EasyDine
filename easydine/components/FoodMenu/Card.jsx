import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image, TouchableOpacity } from 'react-native';
import React, {useState} from 'react';
import { Entypo } from '@expo/vector-icons';
export default function Card(props) {
  const [quantity,setQuantity] = useState(0);
  function handleClick(inp){
    if (inp==0){
      setQuantity(Math.max(quantity-1,0))
      props.removeItem({name:props.name})
    }
    else{
      props.addItem({name:props.name,rate:props.rate})
      setQuantity(quantity+1);
    }
  }
    return (
      <View style={styles.container}>
        <View style={styles.info}>
            <Text>{props.name}</Text>
            <Text>Rate: {props.rate}</Text>
            <View style = {styles.add}>
            <TouchableOpacity title="add" onPress={()=>handleClick(0)}>
              <Entypo name="minus" size={24} color="white" />
              </TouchableOpacity>
              <Text style={styles.quantity}>{quantity}</Text>
              <TouchableOpacity title="add" onPress={()=>handleClick(1)}>
                <Entypo name="plus" size={24} color="white" />
              </TouchableOpacity>
              
            </View>
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
        borderRadius: 10,
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
      height:30,
      backgroundColor:"#5F73F2",
      borderRadius: 10,
      flexDirection:"row",
      justifyContent:"space-around",
      alignItems:"center",
      marginTop:10,
    },
    quantity:{
      color:"white",
      fontWeight: "900"
    }
})
