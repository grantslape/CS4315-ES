import React, { Component } from 'react';
import NavBar from "./NavBar";
import API from './helpers/API';

export default class Search extends Component {
  constructor(props) {
    super(props);

    this.state = {query: '', results: null};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(query) {
    this.setState({ query });
  }

  handleSubmit() {
    let query = this.state.query;

    API.get(`/search?q=${query}`)
      .then(res => {
        const results = res.data;
        this.setState({ results });

        console.log(this.state.results);
      })
  }

  render() {
    return (
      <div>
        <NavBar onChange={this.handleChange} handleSubmit={this.handleSubmit}/>
      </div>
    )
  }
}