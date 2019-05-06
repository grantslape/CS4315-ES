import React, { Component } from 'react';
import { Button, Form, FormControl, Navbar } from "react-bootstrap";
import logo from "./logo.svg";

class NavBar extends Component {
  constructor(props) {
    super(props);

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.props.onChange(event.target.value);
  }

  handleSubmit(event) {
    event.preventDefault();
    this.props.handleSubmit();
  }

  render() {
    const query = this.props.query;

    return (
      <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand>
          <img src={logo} className="App-logo" alt="logo" />GrantSearch
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Form inline onSubmit={this.handleSubmit}>
            <FormControl
              type="text"
              placeholder="Search"
              className="mr-sm-2"
              value={query}
              onChange={this.handleChange}
            />
            <Button variant="outline-success" onClick={this.handleSubmit}>Search</Button>
          </Form>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default NavBar;