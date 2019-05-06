import React, { Component } from 'react';
import { BrowserRouter as Router } from "react-router-dom";
import './App.css';
import Search from "./Search";

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Search />
          <footer className="App-footer">
            Copyright 2019 Grant H. Slape
          </footer>
        </div>
      </Router>
    );
  }
}

export default App;
