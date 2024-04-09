
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View , FlatList, Pressable} from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchDV from '../../src/Dinner/FetchDV';
import FetchDNV from '../../src/Dinner/FetchDNV';
import FetchDD from '../../src/Dinner/FetchDD';

export default function Dinner (){
    const DV = FetchDV();
    const DNV = FetchDNV();
    const DD = FetchDD();
    const Data = DV.concat(DNV, DD);
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