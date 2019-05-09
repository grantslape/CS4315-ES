import React, { Component } from 'react';
import API from '../helpers/API';
import Results from "./Results";

export default class BusinessReviews extends Component {
  constructor(props) {
    super(props);

    this.state = { results: null };
  }

  componentDidMount() {
    const id = this.props.match.params.id;
    API.get(`/search/businesses/${id}/reviews`)
      .then(res => {
        const results = res.data;
        this.setState({ results });
      });
  }


  render() {
    return (
      <Results results={this.state.results}/>
    );
  }
}