import React from 'react';
import { View, Text } from 'react-native';

export default function ViewCartScreen({ route }) {
    // Extract the cart array from the route parameters
    const { cart } = route.params;

    // Now you can use the cart array in your View Cart screen
    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <Text>View Cart Screen</Text>
            {/* Render the contents of the cart array */}
            <Text>Items in Cart: {JSON.stringify(cart)}</Text>
        </View>
    );
}
