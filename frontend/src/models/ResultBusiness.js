import React, { Component } from 'react';

export default class ResultBusiness extends Component {
  render() {
    const business = this.props.business;

    return (
      <div>{JSON.stringify(business)}</div>
    );
  }
}