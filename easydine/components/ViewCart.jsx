import React, {useState} from 'react';
import { View, Text, FlatList, StyleSheet, TouchableOpacity} from 'react-native';
import { useNavigation } from '@react-navigation/native';

export default function ViewCartScreen({ route }) {
    const navigation = useNavigation();
    // Extract the cart array from the route parameters
    const { cart } = route.params;
    let total=0;
    const handlPress = ()=>{
        return (
            navigation.navigate('Checkout', {cart,total})
        );
    }
    const [subTotal,setSubtotal] = useState(0);
    function renderItem (item,index){
        total += item.item.rate * item.item.quantity;
        setSubtotal(total);
        return(
            <View style={styles.item}>
                <Text>{item.item.name}</Text>
                <Text>{item.item.quantity}</Text>
                <Text>{item.item.rate}</Text>
                <Text>{item.item.rate * item.item.quantity}</Text>
            </View>
        )
    }
    // Now you can use the cart array in your View Cart screen
    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
           <View style={styles.item}>
                <Text>Name</Text>
                <Text>units</Text>
                <Text>unit price</Text>
                <Text>Total price</Text>
            </View>
           <FlatList
                data={cart}
                renderItem={renderItem}
                keyExtractor={(item, index) => index.toString()}
                />
                <View style={styles.total}><Text style={styles.totaltext}>Subtotal: {subTotal}</Text></View>
            <TouchableOpacity style={styles.checkout} onPress={handlPress}>
                <Text style={styles.checkouttext}>Checkout</Text>
                </TouchableOpacity>
        </View>
    );
}
const styles = StyleSheet.create({
    item:{
        flexDirection: "row",
        backgroundColor: "white",
        width: 350,
        margin: 10,
        height: 50,
        justifyContent:"space-around",
        alignItems: "center",
        borderRadius: 10,
    },
    checkout:{
        backgroundColor:"#5F73F2",
        height: 50,
        width: 370,
        marginBottom: 20,
        justifyContent: "center",
        alignItems:"center",
        borderRadius:10,
    },
    checkouttext:{
        color:"white",
        fontSize: 25
    },
    total:{
        marginBottom: 20,
        height:50,
        width: 300,
        alignItems: "center"
    },
    totaltext:{
        fontSize: 25,
        color: "#5F73F2",
        fontWeight: "700"
    }
})