import React, { Component } from 'react';
import ResultBusiness from "./ResultBusiness";
import ResultReview from "./ResultReview";

export default class Results extends Component {
  constructor(props) {
    super(props);

    this.state = { results: null };
  }

  parseResults(results) {
    if (results) {
      return results.map((result, index) => {
        if (result.doc_type === 'business') {
          return <ResultBusiness business={result} key={index}/>;
        } else if (result.doc_type === 'review') {
          return <ResultReview review={result} key={index}/>;
        } else {
          return null;
        }
      });
    } else {
      return null;
    }
  }

  // Hydrate the result models
  componentDidUpdate(prevProps, prevState, snapshot) {
    if (this.props.results !== prevProps.results) {
      this.setState({ results: this.parseResults(this.props.results) });
    }
  }

  render() {
    const results = this.state.results;

    if (results !== null && results.length > 0) {
      return (
        <ul className="Results">
          {results}
        </ul>
      );
    }

    return <span>No results</span>;
  }
}