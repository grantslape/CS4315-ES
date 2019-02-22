import React, { Component } from 'react';
import logo from './logo.svg';
import SearchBar from './SearchBar'
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          Grant's Fabulous Search Engine!<br />
          Type your query...
          <SearchBar />
        </header>
        <footer className="App-footer">
          Copyright 2019 Grant H. Slape
        </footer>
      </div>
    );
  }
}

export default App;
