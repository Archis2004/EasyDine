import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image, TouchableOpacity} from 'react-native';
import { useState } from 'react';
import SelectDropdown from 'react-native-select-dropdown'
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
// import { TouchableOpacity } from 'react-native/types';
export default function SelectType(props) {
  let type="";

  const options = [
        {title: 'Veg', icon: '../../assets/veg-symbol'},
        {title: 'Non Veg', icon: '../../assets/non-veg-symbols'},
        {title: 'Dessert', icon: ''},
      ];

    return (
      <View style={styles.container}>
        <TouchableOpacity title={options[1].title} style={styles.option} onPress={()=>props.filter(0)}>
          <Image style={styles.icon} source={require('../../assets/veg-symbol.png')}/>
          <Text>Veg</Text>
        </TouchableOpacity >
        <TouchableOpacity title="veg" style={styles.option} onPress={()=>props.filter(1)}>
        <Image style={styles.icon} source={require('../../assets/non-veg-symbol.png')}/>
        <Text>Non-Veg</Text>
        </TouchableOpacity>
        <TouchableOpacity title="veg" style={styles.option} onPress={()=>props.filter(2)}>
        <Image style={styles.icon} source={require('../../assets/dessert.png')}/>
        <Text>Dessert</Text>
        </TouchableOpacity>
      </View>
    );
  }

const styles = StyleSheet.create({
  container:{
    flexDirection:'row'
  },
  icon:{
    width:20,
    height:20,
    marginRight: 5,
  },
  option:{
    flexDirection:'row',
    backgroundColor: 'white',
    padding: 5,
    paddingLeft: 10,
    paddingRight: 10,
    borderRadius: 10,
    marginHorizontal: 5,
    marginTop: 10,
    marginBottom: 3,
  },
  selected:{
    borderBlockColor:"black"
  }
})