import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import Navbar from "./components/Navbar";
import Test from "./components/Test";
import FoodMenu from './components/FoodMenu/FoodMenu';
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import Login from './components/Login'
import { createContext, useEffect, useState } from 'react';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { FIREBASE_AUTH } from './config';
import { StripeProvider } from '@stripe/stripe-react-native';

const UserContext = createContext();

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
    <StripeProvider publishableKey="pk_test_51P3t9zSGLhh0I8kTcRRh0I5K1q5F9xcUb4ddSVi5y9P4kHD3mpbIiqHtK0LmFQEjl2yElptUniTCCRnjh3Cavi4Z00aRHQ93Ro">
      <NavigationContainer>
        <Stack.Navigator initialRouteName='Login'>
         {user ? (<Stack.Screen name='Inside' component={ InsideLayout } options={{headerShown: false}}/>) : (<Stack.Screen name='Login' component={ Login } options={{headerShown: false}}/>)}
        </Stack.Navigator>
      </NavigationContainer>
    </StripeProvider>
      
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',

  },
});
