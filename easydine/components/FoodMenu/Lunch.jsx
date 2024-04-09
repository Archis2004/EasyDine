import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList, Pressable } from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchLV from '../../src/Lunch/FetchLV';
import FetchLNV from '../../src/Lunch/FetchLNV';
import FetchLD from '../../src/Lunch/FetchLD';

export default function Lunch (){
    const LD = FetchLD();
    const LV = FetchLV();
    const LNV = FetchLNV();
    const Data = LV.concat(LNV, LD);
    return (
        <View style={styles.container}> 
            <SelectType/>
            <View>
            <FlatList
                data={Data}
                renderItem = {({ item }) => (
                    <Pressable
                        style={styles.container}
                    >
                        <Card name={item.name} rate={item.rate} image={item.image} />
                    </Pressable>
                )}
            />
            </View>
        </View>
        
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#E0E0E0',
        flex:1,
    }
})