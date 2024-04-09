import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Image, Pressable } from 'react-native';
import { useState } from 'react';
import SelectDropdown from 'react-native-select-dropdown'
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
export default function SelectType() {
  let type="";
  const [isHighlighted, setIsHighlighted] = useState([0,0,0]);
  let setType=(input,i)=>{
    let out=[0,0,0];
    out[i] = 1;
    setIsHighlighted(out);
  }  
  const dynamicStyles = (i)=>{ backgroundColor: (isHighlighted[i]? 'grey' : 'white')};
  const options = [
        {title: 'Veg', icon: '../../assets/veg-symbol'},
        {title: 'Non Veg', icon: '../../assets/non-veg-symbols'},
        {title: 'Dessert', icon: ''},
      ];

    return (
      <View style={styles.container}>
        <Pressable title={options[1].title} style={[styles.option,(()=>dynamicStyles(0))]} onPress={()=>{setType("veg",0)}}>
          <Image style={styles.icon} source={require('../../assets/veg-symbol.png')}/>
          <Text>Veg</Text>
        </Pressable >
        <Pressable title="veg" style={[styles.option,(()=>dynamicStyles(1))]} onPress={()=>{setType("non-veg",1)}}>
        <Image style={styles.icon} source={require('../../assets/non-veg-symbol.png')}/>
        <Text>Non-Veg</Text>
        </Pressable>
        <Pressable title="veg" style={[styles.option,(()=>dynamicStyles(2))]} onPress={()=>{setType("dessert",2)}}>
        <Image style={styles.icon} source={require('../../assets/dessert.png')}/>
        <Text>Dessert</Text>
        </Pressable>
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