import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, FlatList, Pressable, TouchableOpacity } from 'react-native';
import { FontAwesome5 } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
import SelectType from './SelectType';
import Card from './Card';
import FetchDV from '../../src/Dinner/FetchDV';
import FetchDD from '../../src/Dinner/FetchDD';
import FetchDNV from '../../src/Dinner/FetchDNV';

export default function Dinner() {
    
    const navigation = useNavigation();

    const [cart,setCart] = useState([]);

    function addItem(item){
        let temp = cart;
        for(let i=0;i<temp.length;i++){
            if (temp[i].name ==item.name){
                temp[i].quantity += 1;
                setCart(temp);
                console.log(cart)
                return;
            }
        }
        item.quantity = 1;
        temp.push(item);
        setCart(temp);
        console.log(cart)
    }
    function removeItem(item){
        let temp=cart;
        for(let i=0;i<temp.length;i++){
            if (temp[i].name ==item.name){
                temp[i].quantity -= 1;
                if(temp[i].quantity<=0){
                    temp.splice(i,1);
                };
                setCart(temp);
                console.log(cart)
                return;
            }
        }
    }
    const DV = FetchDV();
    const DNV = FetchDNV();
    const DD = FetchDD();
    
    const dataArray=[DV, DNV, DD];
    const [Data,setData] = useState(DV.concat(DD,DNV));
    let filterStatus = [false,false,false];
    const renderItem = ({ item, index }) => (
        <Pressable style={[styles.itemContainer, (index === Data.length - 1) && styles.lastItem]}>
            <Card name={item.name} rate={item.rate} image={item.image} addItem={addItem} removeItem={removeItem}/>
        </Pressable>
    );

    const handlePress = () => {
        return (
            navigation.navigate('View Cart', {cart})
        );
    };

    const filter=(i)=>{
        let out=[];
        let noFilter = true;
        filterStatus[i]= (!filterStatus[i]);
        for(let i=0;i<3;i++){
            if (filterStatus[i]==true){
                out = out.concat(dataArray[i]);
                nofilter=false;
            }
        };
        if (noFilter==true){
            out=out.concat(DD, DNV, DV);
        }
        setData(out);
        console.log(filterStatus)
    }

    return (
        <View style={styles.container}> 
            <SelectType filter={filter}/>
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