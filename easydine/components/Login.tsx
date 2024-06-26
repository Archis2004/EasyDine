import { View, Text, StyleSheet, TextInput, ActivityIndicator, Button, KeyboardAvoidingView } from 'react-native'
import React, { useState } from 'react'
import { FIREBASE_AUTH } from '../config';
import 'firebase/auth'
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth'
import ReactNativeAsyncStorage from '@react-native-async-storage/async-storage';

const Login = () => {
    
    const [regno, setRegNo] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const auth = FIREBASE_AUTH;

    const storeRegNo = async (reg) => {
        try {
            await ReactNativeAsyncStorage.setItem('regno', reg);
        } catch (error) {
            console.log('Error storing regno:', error);
        }
    }

    const signIn = async () => { 
        setLoading(true);
        try {
            const response = await signInWithEmailAndPassword(auth, regno.concat('@gmail.com'), password);
            console.log(response);
            await storeRegNo(regno);
        } catch (error: any) { 
            console.log(error);
            alert('Sign in failed: ' + error.message)
        } finally {
            setLoading(false);
        }
    }

    const signUp = async () => { 
        setLoading(true);
        try {
            const response = await createUserWithEmailAndPassword(auth, regno.concat('@gmail.com'), password);
            console.log(response);
            await storeRegNo(regno);
            alert("Check your email!");
        } catch (error: any) { 
            console.log(error);
            alert('Sign in failed: ' + error.message)
        } finally {
            setLoading(false);
        }
    }


    return (
        <View style={styles.container}>
            <KeyboardAvoidingView behavior='padding'>
                <TextInput value={regno} style={styles.input} placeholder='RegNo' autoCapitalize='none' onChangeText={(text) => setRegNo(text)}></TextInput>
                <TextInput value={password} style={styles.input} secureTextEntry={ true } placeholder='Password' autoCapitalize='none' onChangeText={(text) => setPassword(text)}></TextInput>

                {loading ? <ActivityIndicator size='large' color='#0000ff' />  
                    : <>
                        <Button title='Login' onPress={signIn} />
                        <Button title='Create account' onPress={signUp} />
                    </>
                }
            </KeyboardAvoidingView>
        </View>
    );
};

export default Login;

const styles = StyleSheet.create({
    container: {
        marginHorizontal: 20,
        flex: 1,
        justifyContent: 'center'
    },
    input: {
        marginVertical: 4,
        height: 50,
        borderWidth: 1,
        borderRadius: 4,
        padding: 10,
        backgroundColor: '#fff'
    },
    login: {
        marginVertical: 4,
        height: 50,
        borderWidth: 1,
        borderRadius: 4,
        padding: 10,
        backgroundColor: '#fff'
    },
    create: {
        marginVertical: 4,
        height: 50,
        borderWidth: 1,
        borderRadius: 4,
        padding: 10,
        backgroundColor: '#fff'
    }
});
