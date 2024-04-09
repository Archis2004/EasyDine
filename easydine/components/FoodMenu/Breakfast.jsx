import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, FlatList, Pressable, TouchableOpacity } from 'react-native';
import { FontAwesome5 } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
import SelectType from './SelectType';
import Card from './Card';
import FetchBV from '../../src/Breakfast/FetchBV';
import FetchBB from '../../src/Breakfast/FetchBB';
import FetchBNV from '../../src/Breakfast/FetchBNV';

export default function Breakfast() {
    
    const navigation = useNavigation();

    const [cart,setCart] = useState([]);

    function addItem(item){
        let temp = cart;
        for(let i=0;i<temp.length;i++){
            if (temp[i].name ==item.name){
                temp[i].quantity += 1;
                setCart(temp);
                return;
            }
        }
        item.quantity = 1;
        temp.push(item);
        setCart(temp);
        console.log()
    }
    const BV = FetchBV();
    const BNV = FetchBNV();
    const BB = FetchBB();
    const Data = BV.concat(BNV, BB);

    const renderItem = ({ item, index }) => (
        <Pressable style={[styles.itemContainer, index === Data.length - 1 && styles.lastItem]}>
            <Card name={item.name} rate={item.rate} image={item.image} />
        </Pressable>
    );

    const handlePress = () => {
        return (
            navigation.navigate('View Cart')
        );
    };

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
            <View style={styles.cart}>
                <TouchableOpacity style={styles.cartButton} onPress={handlePress}>
                <FontAwesome5 style={styles.cartIcon} name="shopping-cart" size={24} color="white" />
                <Text style={styles.cartText}>
                    View Cart</Text>
                </TouchableOpacity>  
            </View>

        </View>
        
      );
};

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#E0E0E0',
        flex:1,
    },
    flatListContainer: {
        flex: 1,
    },
    itemContainer: {
        marginBottom: 0, // Default marginBottom
    },
    lastItem: {
        marginBottom: 70, // Increase marginBottom for the last item
    },
    cart:{
        position: 'absolute',
        width: "100%",
        height: "10%",
        left :0,
        right: 0,
        bottom: 0,
        padding: 5,
        flexDirection: "column",
        justifyContent: "space-around",
        backgroundColor:"#E0E0E0",
        
    },
    cartButton:{
        backgroundColor:"#2C58E8",
        height:"90%",
        justifyContent:"center",
        alignItems:"center",
        borderRadius:10,
        flexDirection:"row",

    },
    cartText:{
        color:"white",
        fontWeight: "bold",
        marginLeft:20,
    },
    cartIcon:{
    }
})