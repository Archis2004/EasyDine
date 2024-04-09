import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList, Pressable } from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchLV from '../../src/Lunch/FetchLV';
import FetchLNV from '../../src/Lunch/FetchLNV';
import FetchLD from '../../src/Lunch/FetchLD';

export default function Lunch (){
  const DATA=FetchLD();
    return (
        <View style={styles.container}>
          {/* <FetchLV />
          <FetchLNV /> */}
          {/* <FetchLD /> */}
          <card
          {/* <SelectType/> */}
          <FlatList
                data={DATA}
                renderItem = {({ item }) => (
                    <Pressable
                        style={styles.container}
                    >
                        {/* <View style={styles.innerContainer}>
                            <Text style={styles.innerName}>{item.name}</Text>
                            <Text style={styles.innerQty}>{item.quantity}</Text>
                            <Text style={styles.innerRate}>{item.rate}</Text>
                        </View> */}
                        <Card name={item.name} rate={item.rate}/>
                    </Pressable>
                )}
            />
        </View>
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#E0E0E0',
        flex:1,
    }
})