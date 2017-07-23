import React from 'react';
import {
  Text,
  View,
} from 'react-native';

import {
  StackNavigator,
} from 'react-navigation';

class HomeScreen extends React.Component {
  static navigationOptions = {
    title: 'Home'
  };

  render() {
    return (
      <View style={{alignItems: 'center', justifyContent: 'center', flex: 1}}>
        <Text onPress={this._handlePress}>Go To Leo!</Text>
      </View>
    )
  }

  _handlePress = () => {
    this.props.navigation.navigate('Leo');
  }
}

class LeoScreen extends React.Component {
  static navigationOptions = {
    title: 'Leo'
  };

  render() {
    return (
      <View style={{alignItems: 'center', justifyContent: 'center', flex: 1}}>
        <Text>This is the Leo Screen</Text>
        <Text onPress={this._handlePress}>DePaq Screen!</Text>
      </View>
    )
  }

  _handlePress = () => {
    this.props.navigation.navigate('DePaq');
  }
}

class DePaqScreen extends React.Component {
  static navigationOptions = {
    title: 'DePaq'
  };

  render() {
    return (
      <View style={{alignItems: 'center', justifyContent: 'center', flex: 1}}>
 
        <Text onPress={this._handlePress}>Go to HomeScreen!</Text>
      </View>
    )
  }

  _handlePress = () => {
    this.props.navigation.navigate('Home');
  }
}

export default StackNavigator({
  Home: {
    screen: HomeScreen,
  },
  Leo: {
    screen: LeoScreen,
  },
  DePaq: {
    screen: DePaqScreen,
  },
});
