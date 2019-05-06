import React, { Component } from 'react';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import {Link} from "react-router-dom";

export default class ResultBusiness extends Component {
  render() {
    const business = this.props.business;

    return (
      <Container>
        <Row>
          <Col xs={6}>
            <Link to={`/businesses/${business.id}`}>
              {business.name}
            </Link>
          </Col>
          <Col xs={6}>
            Hours go here
          </Col>
        </Row>
        <Row>
          <Col xs={6}>
            {business.address}<br/>
            {business.city}, {business.state} {business.postal_code}
          </Col>
          <Col>
            Stars: {business.stars} <br/>
            Reviews: {business.review_count}
          </Col>
        </Row>
        <Row>
          <Col>
            {business.categories && business.categories.join(', ')}
          </Col>
        </Row>
      </Container>
    );
  }
}