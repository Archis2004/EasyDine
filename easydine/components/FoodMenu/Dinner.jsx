
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SelectType from './SelectType';
import FetchDV from '../../src/Dinner/FetchDV';
import FetchDNV from '../../src/Dinner/FetchDNV';
import FetchDD from '../../src/Dinner/FetchDD';

export default function Dinner (){
    return (
      <View style={styles.container}>
          <FetchDV />
          <FetchDNV />
          <FetchDD />
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