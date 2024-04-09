import React from 'react';
import { View, StyleSheet, FlatList, Pressable } from 'react-native';
import SelectType from './SelectType';
import Card from './Card';
import FetchLV from '../../src/Lunch/FetchLV';
import FetchLNV from '../../src/Lunch/FetchLNV';
import FetchLD from '../../src/Lunch/FetchLD';

export default function Lunch() {
    const LD = FetchLD();
    const LV = FetchLV();
    const LNV = FetchLNV();
    const Data = LV.concat(LNV, LD);

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
