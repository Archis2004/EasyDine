import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import {NavigationContainer} from '@react-navigation/native';
import VegMenu from './VegMenu';
import NonvegMenu from './NonvegMenu';
import SpecialMenu from './SpecialMenu';
const Tab = createMaterialTopTabNavigator();

export default function FoodMenu (){
    return (

        <Tab.Navigator>
          <Tab.Screen name="veg" component={VegMenu} />
          <Tab.Screen name="nonveg" component={NonvegMenu} />
          <Tab.Screen name="special" component={SpecialMenu} />
        </Tab.Navigator>

      );
};

const styles = StyleSheet.create({

})