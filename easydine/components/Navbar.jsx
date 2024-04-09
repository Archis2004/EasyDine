import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Entypo } from '@expo/vector-icons';

export default function Navbar() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        EasyDine
      <Entypo style={styles.menuicon} name="menu" size={24} color="white" />
      </Text>
      
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
    container: {

      width: '100%',
      backgroundColor: '#A81616',
      color:'#fff',
      justifyContent: 'center',
    },
    title:{
        display:'flex',
        flexDirection:'row',
        padding:13,
        paddingTop:30,
        fontSize:20,
        color:'#fff',
    },
    menuicon:{
        position: 'absolute',
        right:0,
    },
  });