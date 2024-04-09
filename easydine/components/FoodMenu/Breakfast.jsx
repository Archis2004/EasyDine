import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList, Pressable } from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchBV from '../../src/Breakfast/FetchBV';
import FetchBB from '../../src/Breakfast/FetchBB';
import FetchBNV from '../../src/Breakfast/FetchBNV';

export default function Breakfast (){
    const BV = FetchBV();
    const BNV = FetchBNV();
    const BB = FetchBB();
    const Data = BV.concat(BNV, BB);
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