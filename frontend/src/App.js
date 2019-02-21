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
        </header>
        <body className="App-body">
          <SearchBar />
        </body>
      </div>
    );
  }
}

export default App;
