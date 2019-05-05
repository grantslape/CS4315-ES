import React, { Component } from 'react';

export default class ResultReview extends Component {
  render() {
    const review = this.props.review;

    return (
      <div>{JSON.stringify(review)}</div>
    );
  }
}