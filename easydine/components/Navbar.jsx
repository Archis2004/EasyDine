import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function Navbar() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>EasyDine</Text>
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
        padding:13,
        paddingTop:30,
        fontSize:20,
        color:'#fff',
    },
  });