import React, { Component } from 'react';

export default class Results extends Component {
  render() {
    const results = this.props.results;

    if (results !== null) {
      return (
        <ul>
          {results.map((result, i) => <li key={i} className="Result">{JSON.stringify(result)}<hr/></li>)}
        </ul>
      );
    }

    return <span>No results</span>;
  }
}