import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SelectType from './SelectType';

export default function Breakfast (){
    return (
        <View style={styles.container}>
          <SelectType/>
          {/* <FlatList 
          /> */}
        </View>
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'red',
        flex:1,
    }
})