import React, { Component } from 'react';
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import { Markup } from 'interweave';

export default class ResultReview extends Component {
  render() {
    const review = this.props.review;

    return (
      <Container>
        <Row>
          <Col xs={12} md={6}>
            {review.business_id}
          </Col>
          <Col xs={12} md={6}>
            {review.user_id}
          </Col>
        </Row>
        <Row>
          <Col xs={12}>
            <Markup content={review.highlights[0]}/>
          </Col>
        </Row>
        <Row>
          <Col xs={4}>
            S: {review.stars} C: {review.cool} J: {review.funny} U: {review.useful}
          </Col>
          <Col xs={8}>
            {review.date}
          </Col>
        </Row>
      </Container>
    );
  }
}