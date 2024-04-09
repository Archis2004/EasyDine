import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View, Button } from 'react-native';
import React from 'react';
import { NavigatorProp } from '@react-navigation/native'
import { FIREBASE_AUTH } from '../config';

export default function Profile() {

    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        {/* <Button onPress={() => navigation.navigate('details')} title='Open Details' /> */}
        <Button onPress={() => FIREBASE_AUTH.signOut()} title='LogOut' />
      </View>
    );
  }

const styles = StyleSheet.create({

})