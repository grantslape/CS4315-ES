import React, { Component } from 'react';
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import API from '../helpers/API';
import {Link} from "react-router-dom";

export default class Business extends Component {
  constructor(props) {
    super(props);

    this.state = { business: null };
  }

  componentDidMount() {
    const id = this.props.match.params.id;

    API.get(`/doc/businesses/${id}`)
      .then(res => {
        const business = res.data;
        this.setState({ business });
      });
  }


  render() {
    if (this.state.business) {
      const business = this.state.business;
      const id = this.props.match.params.id;

      return (
        <Container>
          <Row>
            <Col xs={12}>
              {business.name}
            </Col>
          </Row>
          <Row>
            <Col xs={6}>
              {business.address} <br/>
              {business.city}, {business.state} {business.postal_code}
            </Col>
            <Col xs={6}>
              Stars: {business.stars}<br/>
              Reviews:&nbsp;
              <Link to={`/businesses/${id}/reviews`}>
                {business.review_count}
              </Link>
            </Col>
          </Row>
          <Row>
            <Col>
              Categories:<br/>
              {business.categories.join(', ')}
            </Col>
          </Row>
        </Container>
      );
    } else {
      return null;
    }
  }
}