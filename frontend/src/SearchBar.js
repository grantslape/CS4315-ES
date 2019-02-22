import React, { Component } from 'react';

class SearchBar extends Component {
  render() {
    return (
      <form>
         <label>
            <input type="text" autoFocus placeholder="Enter query" />
          </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default SearchBar;
