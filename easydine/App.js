import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import Navbar from "./components/Navbar";
import Test from "./components/Test";
import FoodMenu from './components/FoodMenu/FoodMenu';

export default function App() {
  return (
         <NavigationContainer>
          <Navbar/>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',

  },
});
