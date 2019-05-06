import React, { Component } from 'react';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col"
import API from '../helpers/API';

export default class Review extends Component {
  constructor(props) {
    super(props);

    this.state = { review: null };
  }

  componentDidMount() {
    const id = this.props.match.params.id;

    API.get(`/doc/reviews/${id}`)
      .then(res => {
        const review = res.data;
        this.setState({ review })
      });
  }


  render() {
    if (this.state.review) {
      const review = this.state.review;

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
            <Col xs={8}>
              {review.date}
            </Col>
            <Col xs={4}>
              S: {review.stars}
            </Col>
          </Row>
          <Row>
            <Col>
              {review.text}
            </Col>
          </Row>
          <Row>
            <Col>
              C: {review.cool} J: {review.funny} U: {review.useful}
            </Col>
          </Row>
        </Container>
      );
    } else {
      return null;
    }
  }
}