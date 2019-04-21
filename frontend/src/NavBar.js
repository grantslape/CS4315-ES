import React, { Component } from 'react';
import {Button, Form, FormControl, Nav, Navbar, NavDropdown} from "react-bootstrap";
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
    this.props.handleSubmit();
  }

  render() {
    const query = this.props.query;

    return (
      <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand href="#home">
          <img src={logo} className="App-logo" alt="logo" />GrantSearch
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          {/*<Nav className="mr-auto">*/}
          {/*  <Nav.Link href="#home">Home</Nav.Link>*/}
          {/*  <Nav.Link href="#link">Link</Nav.Link>*/}
          {/*  <NavDropdown title="Dropdown" id="basic-nav-dropdown">*/}
          {/*    <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>*/}
          {/*    <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>*/}
          {/*    <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>*/}
          {/*    <NavDropdown.Divider />*/}
          {/*    <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>*/}
          {/*  </NavDropdown>*/}
          {/*</Nav>*/}
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