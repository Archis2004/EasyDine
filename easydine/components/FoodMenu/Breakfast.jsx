import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SelectType from './SelectType';
import Fetch from './src/Fetch';

export default function Breakfast (){
    return (
        <View style={styles.container}>
          <Fetch/>
        </View>
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'red',
        flex:1,
    }
})