import React, { Component } from 'react';
import './App.css';
import NavBar from './NavBar.js'

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar />
        <footer className="App-footer">
          Copyright 2019 Grant H. Slape
        </footer>
      </div>
    );
  }
}

export default App;
