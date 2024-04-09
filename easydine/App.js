import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import Navbar from "./components/Navbar";
import Test from "./components/Test";
import FoodMenu from './components/FoodMenu/FoodMenu';
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import Login from './components/Login'
import { useEffect, useState } from 'react';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { FIREBASE_AUTH } from './config';

const Stack = createNativeStackNavigator();

const InsideStack = createNativeStackNavigator();

function InsideLayout() {
  return (
    <InsideStack.Navigator>
      <InsideStack.Screen name='navbar' component={Navbar} options={{headerShown: false}} />
    </InsideStack.Navigator>
  );
}

export default function App() {
  const [user, setUser] = useState (null);
  
  useEffect(() => {
    onAuthStateChanged(FIREBASE_AUTH, (user) => {
      setUser(user);
    });
  }, []);
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='Login'>
        {user ? (<Stack.Screen name='Inside' component={ InsideLayout } options={{headerShown: false}}/>) : (<Stack.Screen name='Login' component={ Login } options={{headerShown: false}}/>)}
      </Stack.Navigator>
      {/* <Navbar/> */}
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
