import React, { Component } from 'react';

class AppHeader extends Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
      <nav id="nav" style={{background: "#2b252c"}}>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/Nonprofits">Nonprofits</a></li>
          <li><a href="/Categories">Categories</a></li>
          <li><a href="/Locations">Locations</a></li>
          <li><a href="/About">About</a></li>
          <li><a href="/all/search">Search</a></li>
        </ul>
      </nav>
    );
  }
}

export default AppHeader;
