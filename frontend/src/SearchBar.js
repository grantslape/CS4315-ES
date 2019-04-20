import React, { Component } from 'react';

class SearchBar extends Component {
  constructor(props) {
    super(props);
    this.state = {query: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({query: event.target.value});
  }

  handleSubmit(event) {
    alert('Search query would be: ' + this.state.query);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
         <label>
            <input 
              type="text"
              autoFocus
              placeholder="Enter query"
              value={this.state.query}
              onChange={this.handleChange}
            />
          </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default SearchBar;
