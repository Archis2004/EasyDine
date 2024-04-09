import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SelectType from './SelectType';
import FetchBV from '../../src/Breakfast/FetchBV';
import FetchBB from '../../src/Breakfast/FetchBB';
import FetchBNV from '../../src/Breakfast/FetchBNV';

export default function Breakfast (){
    return (
        <View style={styles.container}>
          <FetchBV />
          <FetchBB />
          <FetchBNV />
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