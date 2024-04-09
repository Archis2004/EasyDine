import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View } from 'react-native';
import SelectDropdown from 'react-native-select-dropdown'

export default function SelectType() {
    let DATA=[1,2,3,4,5,6]

    return (
      <View style={styles.container}>
        <SelectDropdown 
        data={DATA}
        renderButton={(selectedItem,isOpened)=>{
            return <Text>{selectedItem}</Text>
        }}
        renderItem={(item, index, isSelected)=>{
            return <Text>{item}</Text>
        }}/>
      </View>
    );
  }

const styles = StyleSheet.create({

})