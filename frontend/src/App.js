import React, { Component } from 'react';
import './App.css';
import Search from "./Search";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Search />
        <footer className="App-footer">
          Copyright 2019 Grant H. Slape
        </footer>
      </div>
    );
  }
}

export default App;
