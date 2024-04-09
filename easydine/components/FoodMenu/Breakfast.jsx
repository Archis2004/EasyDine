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
    const renderItem = ({ item, index }) => (
        <Pressable style={[styles.itemContainer, index === Data.length - 1 && styles.lastItem]}>
            <Card name={item.name} rate={item.rate} image={item.image} />
        </Pressable>
    );

    return (
        <View style={styles.container}>
            <SelectType />
            <View style={styles.flatListContainer}>
                <FlatList
                    data={Data}
                    renderItem={renderItem}
                    keyExtractor={(item, index) => index.toString()}
                />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#E0E0E0',
        flex: 1,
    },
    flatListContainer: {
        flex: 1,
    },
    itemContainer: {
        marginBottom: 0, // Default marginBottom
    },
    lastItem: {
        marginBottom: 75, // Increase marginBottom for the last item
    },
});
