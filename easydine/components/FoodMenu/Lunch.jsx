import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchLV from '../../src/Lunch/FetchLV';
import FetchLNV from '../../src/Lunch/FetchLNV';
import FetchLD from '../../src/Lunch/FetchLD';

export default function Lunch (){
    return (
        <View style={styles.container}>
          <Card/>
          <FetchLV />
          <FetchLNV />
          <FetchLD />
          {/* <SelectType/> */}
          {/* <FlatList 
          /> */}
        </View>
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#E0E0E0',
        flex:1,
    }
})