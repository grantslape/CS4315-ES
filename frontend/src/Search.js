import React, { Component } from 'react';
import NavBar from "./NavBar";
import API from './helpers/API';
import Results from "./Results";
import ResultBusiness from "./models/ResultBusiness";
import ResultReview from "./models/ResultReview";

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
        const response = res.data;
        console.log(response);

        const results = response.map((result, index) => {
          if (result.doc_type === 'business') {
            return <ResultBusiness business={result} key={index}/>;
          } else if (result.doc_type === 'review') {
            return <ResultReview review={result} key={index}/>;
          } else {
            return null;
          }
        });

        this.setState({ results });
      })
  }

  render() {
    return (
      <div>
        <NavBar onChange={this.handleChange} handleSubmit={this.handleSubmit}/>
        <Results results={this.state.results}/>
      </div>
    )
  }
}