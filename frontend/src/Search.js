import React, { Component } from 'react';
import NavBar from "./NavBar";

export default class Search extends Component {
  constructor(props) {
    super(props);

    this.state = {query: '', results: null};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(query) {
    this.setState({query});
  }

  handleSubmit() {
    //TODO: make query
    console.log(this.state.query);
  }

  render() {
    return (
      <div>
        <NavBar onChange={this.handleChange} handleSubmit={this.handleSubmit}/>
      </div>
    )
  }
}