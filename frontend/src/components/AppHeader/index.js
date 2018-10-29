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
          <li><a href="/nonprofits">Nonprofits</a></li>
          <li><a href="/categories">Categories</a></li>
          <li><a href="/locations">Locations</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </nav>
    );
  }
}

export default AppHeader;
