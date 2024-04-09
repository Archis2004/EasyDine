import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View } from 'react-native';

export default function Credits() {
  const DATA = {amount: 2311,};
  const now = new Date();
  const days = now.getDate();
  const firstDayOfNextMonth = new Date(now.getFullYear(), now.getMonth() + 1, 1);
  const lastDayOfCurrentMonth = new Date(firstDayOfNextMonth - 1);
  const daysInMonth = lastDayOfCurrentMonth.getDate();
    return (
      <View style={styles.outer}>
        <View style={styles.current}>
          <View><Text style={styles.label}>Current Credits: </Text>
        <Text style={styles.amount}>{DATA.amount} </Text></View>
        </View>

          <View style={styles.current}>
          <Text style={styles.label}>Credits Spent per day:</Text>
          <Text style={styles.amount}>{(Math.floor((6180 - DATA.amount)/days))}</Text>
          </View>
          
          <View style={styles.current}>
          <Text style={styles.label}>Credits Remaining per day:</Text>
          <Text style={styles.amount}>{(Math.floor((DATA.amount)/(daysInMonth-days)))}</Text>
          </View>
      </View>
    );
  }

const styles = StyleSheet.create({
  outer:{
    padding:20,
    flex:1,
    backgroundColor:"#F8F6E3"
  },
  current:{
    height:"30%",
    borderRadius:20,
    padding:20,
    marginBottom: 20,
    backgroundColor : "#C4E4FF",
  },
  label:{
    fontSize:20,
    color:"#000FFF",
  },
  amount:{
    fontSize:70,
    fontWeight:"400",
    color:"#000FFF",
  },
  perDays:{
    backgroundColor:"white"
  }
})