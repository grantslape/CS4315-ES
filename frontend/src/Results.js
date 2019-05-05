import React, { Component } from 'react';

export default class Results extends Component {

  render() {
    const results = this.props.results;

    if (results !== null && results.length > 0) {
      return (
        <ul>
          {results}
        </ul>
      );
    }

    return <span>No results</span>;
  }
}