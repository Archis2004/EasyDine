import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import {NavigationContainer} from '@react-navigation/native';
import Dinner from './Dinner';
import Breakfast from './Breakfast';
import Lunch from './Lunch';
const Tab = createMaterialTopTabNavigator();

export default function FoodMenu (){
    return (
      
        <Tab.Navigator>
          <Tab.Screen name="Breakfast" component={Breakfast} />
          <Tab.Screen name="Lunch" component={Lunch} />
          <Tab.Screen name="Dinner" component={Dinner} />
        </Tab.Navigator>

      );
};

const styles = StyleSheet.create({

})