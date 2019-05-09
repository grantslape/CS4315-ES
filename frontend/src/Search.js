import React, { Component } from 'react';
import NavBar from "./NavBar";
import API from './helpers/API';
import Results from "./models/Results";
import Review from "./models/Review";
import Business from "./models/Business";
import {Route, withRouter} from "react-router-dom";
import BusinessReviews from "./models/BusinessReviews";

class Search extends Component {
  constructor(props) {
    super(props);

    this.state = { query: '', results: null };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(query) {
    this.setState({ query });
  }

  handleSubmit() {
    const query = this.state.query;
    this.getData(query);
  }

  getData(query) {
    API.get(`/search?q=${query}`)
      .then(res => {
        const results = res.data;
        console.log(results);
        this.setState({ results });
        this.props.history.push({ pathname: '/search', search: `q=${query}` });
      });
  }

  setQueryString() {
    const queryString = require('query-string');
    const q = queryString.parse(this.props.location.search).q;
    if (q !== undefined) {
      this.setState({ query: q });
      this.getData(q);
    }
  }

  componentDidMount() {
    this.setQueryString();
  }

  render() {
    return (
      <div>
        <NavBar onChange={this.handleChange} handleSubmit={this.handleSubmit} query={this.state.query}/>
        <Route
          path={"/search"}
          render={
            (props) => <Results {...props} results={this.state.results}/>
          }
        />
        <Route path={"/reviews/:id"} component={Review}/>
        <Route path={"/businesses/:id"} component={Business}/>
        <Route path={"/businesses/:id/reviews"} component={BusinessReviews}/>
      </div>
    )
  }
}

export default withRouter(Search)