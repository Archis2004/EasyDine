import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Entypo } from '@expo/vector-icons';
import FoodMenu from './FoodMenu/FoodMenu';
import Profile from './Profile';
import Credits from './Credits';
import Orders from './Orders';
import Settings from './Settings';
import ViewCart from './ViewCart';
import Checkout from './Checkout';
const Drawer = createDrawerNavigator();

export default function Navbar() {

  return (
      
      <Drawer.Navigator name="EasyDine" options={{ drawerLabel: 'Custom Name' }}>
      <Drawer.Screen name="Menu" component={FoodMenu}/>
      <Drawer.Screen name="Profile" component={Profile}/>
      <Drawer.Screen name="Credits" component={Credits}/>
      {/* <Drawer.Screen name="Past Orders" component={Orders} /> */}
      <Drawer.Screen name="Settings" component={Settings} />
      <Drawer.Screen name="Checkout" component={Checkout} options={{ drawerLabel: () => { null } }} />
      <Drawer.Screen name="View Cart" component={ViewCart} options={{drawerLabel:()=>{null}}} />
      </Drawer.Navigator>
      
  );
}

const styles = StyleSheet.create({
    container: {

      width: '100%',
      backgroundColor: '#A81616',
      color:'#fff',
      justifyContent: 'center',
    },
    title:{
        display:'flex',
        flexDirection:'row',
        padding:13,
        paddingTop:30,
        fontSize:20,
        color:'#fff',
    },
    menuicon:{
        position: 'absolute',
        right:0,
    },
  });